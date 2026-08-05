"""
Unit tests for the Student Grade Tracker.

These tests automatically verify that important
functions return the expected values.
"""

import unittest
import os

from gradebook import (
    add_student,
    add_score,
    calculate_average,
    letter_grade,
    class_average,
    save_students,
    load_students,
    delete_student
)

class TestGradebook(unittest.TestCase):

    def setUp(self):
        # Create a fresh gradebook before every test.
        self.students = {}

    def test_add_student(self):
        # Test Adding students.
        add_student(self.students, "Alice")
        self.assertIn("Alice", self.students)
        self.assertEqual(self.students["Alice"], [])

    def test_add_scores(self):
        # Test Scores being added
        add_student(self.students, "Bob")
        add_score(self.students, "Bob", 95)
        add_score(self.students, "Bob", 85)

        self.assertEqual(self.students["Bob"], [95, 85])

    def test_average(self):
        # Test average of scores.
        self.assertEqual(calculate_average([100, 90, 80]), 90.0)

    def test_average_empty(self):
        # Test an empty average.
        self.assertEqual(calculate_average([]), 0)

    def test_letter_grade(self):
        # Testing each letter grade.
        self.assertEqual(letter_grade(95), "A")
        self.assertEqual(letter_grade(84), "B")
        self.assertEqual(letter_grade(73), "C")
        self.assertEqual(letter_grade(61), "D")
        self.assertEqual(letter_grade(20), "F")

    def test_class_average(self):
        # Testing multiple student scores add to correct average.
        add_student(self.students, "Alice")
        add_student(self.students, "Bob")

        add_score(self.students, "Alice", 90)
        add_score(self.students, "Alice", 100)

        add_score(self.students, "Bob", 80)
        add_score(self.students, "Bob", 90)

        self.assertEqual(class_average(self.students), 90.0)

    def test_save_and_load(self):
        # Testing saving and loading students across sessions.
        add_student(self.students, "Charlie")
        add_score(self.students, "Charlie", 88)

        save_students(self.students)

        loaded = load_students()

        self.assertIn("Charlie", loaded)
        self.assertEqual(loaded["Charlie"], [88])

    def test_delete_student(self):
        # Testing deleting students from roster.
        add_student(self.students, "David")
        self.assertTrue(delete_student(self.students, "David"))
        self.assertNotIn("David", self.students)

    def test_delete_missing_student(self):
        # Testing imaginary student deletion.
        self.assertFalse(delete_student(self.students, "Nobody"))

    def test_full_workflow(self):
        # Simulating a complete user session.

        add_student(self.students, "Emma")

        add_score(self.students, "Emma", 100)
        add_score(self.students, "Emma", 90)
        add_score(self.students, "Emma", 80)

        avg = calculate_average(self.students["Emma"])

        self.assertEqual(avg, 90.0)
        self.assertEqual(letter_grade(avg), "A")

        save_students(self.students)

        loaded = load_students()

        self.assertEqual(loaded["Emma"], [100, 90, 80])

        delete_student(loaded, "Emma")

        self.assertNotIn("Emma", loaded)

if __name__ == "__main__":
    unittest.main()
