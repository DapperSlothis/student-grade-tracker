import unittest
from gradebook import calculate_average,letter_grade

class T(unittest.TestCase):
    def test_avg(self): self.assertEqual(calculate_average([100,90,80]),90.0)
    def test_empty(self): self.assertEqual(calculate_average([]),0)
    def test_grade(self): self.assertEqual(letter_grade(95),"A")
if __name__=="__main__":
    unittest.main()
