"""
gradebook.py

This file contains all of the functions used to manage the
student grade book.

These functions allow the program to:

• Load student data
• Save student data
• Add students
• Add grades
• Calculate averages
• Determine letter grades
• Calculate class statistics
"""

import json, os

DATA_FILE="students.json"

def load_students():
    """
    Loads student information from the JSON file.

    If the file exists, the data is read and converted
    into a Python dictionary.

    If the file does not exist, an empty dictionary is
    returned so the program can start with no students.
    """
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE) as f: return json.load(f)
    return {}

def save_students(data):
    """
    Saves the current student dictionary into the JSON file.

    This allows all student information to remain available
    the next time the program is started.
    """
    with open(DATA_FILE,'w') as f: json.dump(data,f,indent=2)

def add_student(data,name):
    """
    Adds a new student to the dictionary.

    Each student is stored as a key, and their grades are
    stored in a list.

    If the student already exists, nothing changes.
    """
    if name not in data: data[name]=[]

def add_score(data,name,score):
    """
    Adds a new test score to an existing student.

    The score is appended onto the student's list
    of grades.
    """
    data[name].append(score)

def calculate_average(scores):
    """
    Calculates the average score for one student.

    If there are no scores, the function returns 0
    instead of causing a divide-by-zero error.
    """
    return round(sum(scores)/len(scores),1) if scores else 0

def letter_grade(avg):
    """
    Converts a numeric average into a letter grade.

    90-100 = A
    80-89 = B
    70-79 = C
    60-69 = D
    Below 60 = F
    """
    return "A" if avg>=90 else "B" if avg>=80 else "C" if avg>=70 else "D" if avg>=60 else "F"

def class_average(data):
    """
    Calculates the average score for the entire class.

    It first calculates each student's average, then
    averages those values together.
    """
    avgs=[calculate_average(v) for v in data.values() if v]
    return calculate_average(avgs)

def delete_student(data, name):
    """
    Deletes a student from the grade book.

    Parameters:
        data (dict): Dictionary containing student records.
        name (str): Name of the student to remove.

    Returns:
        bool:
            True if the student existed and was removed.
            False if the student was not found.
    """
    if name in data:
        del data[name]
        return True
    return False
