"""
Program: student_test.py
Author: Spencer Cress
Date: 7/1/2020

Tests of student class for Unit Test for a Class assignment
"""
import unittest
from class_definitions.student import Student


class MyTestCase(unittest.TestCase):
    def setUp(self):
        """Sets up a student object"""
        self.student = Student('Duck', 'Daisy', 'AAS', 4.0)

    def tearDown(self):
        """Tears down a student object"""
        del self.student

    def test_initial_value_required_attributes(self):
        """Tests all required attributes of Student class"""
        self.assertEqual(self.student.last_name, 'Duck')
        self.assertEqual(self.student.first_name, 'Daisy')
        self.assertEqual(self.student.major, 'AAS')
        #self.assertEqual(self.student.gpa, 4.0)

    def test_inital_all_attributes(self):
        """Tests all attributes of Student class"""
        aStudent = Student('Duck', 'Daisy', 'AAS', 4.0)
        assert aStudent.last_name == 'Duck'
        assert aStudent.first_name == 'Daisy'
        assert aStudent.major == 'AAS'
        assert aStudent.gpa == 4.0

    def test_student_str(self):
        """Tests string output function inside Student class"""
        self.assertEqual(str(self.student), 'Duck, Daisy has major AASwith gpa: 4.0')

    def test_object_not_created_error_last_name(self):
        """Tests error output if first parameter 'last_name' is not entered or out of bounds in Student class"""
        with self.assertRaises(ValueError):
            aStudent = Student()

    def test_object_not_created_error_fist_name(self):
        with self.assertRaises(ValueError):
            """Tests error output if second parameter 'first_name' is not entered or out of bounds in Student class"""
            aStudent = Student('Duck', '896')

    def test_object_not_created_error_major(self):
        """Tests error output if third parameter 'major' is not entered or out of bounds in Student class"""
        with self.assertRaises(ValueError):
            aStudent = Student('Duck', 'Daisy')

    def test_object_not_created_error_gpa(self):
        """Tests error output if fourth parameter 'gpa' is out of bounds as string rather than float in Student class"""
        with self.assertRaises(ValueError):
            aStudent = Student('Duck', 'Daisy', 'AAS', 'Bad')

    def test_object_not_in_range_error_gpa(self):
        """Tests error output if fourth parameter 'gpa' is out of bounds as negative rather than 0 - 5.0 in Student class"""
        with self.assertRaises(ValueError):
            aStudent = Student('Duck', 'Daisy', 'AAS', -1.0)


if __name__ == '__main__':
    unittest.main()
