import unittest
from class_definitions.student import Student


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = Student('Duck', 'Daisy', 'AAS', 4.0)

    #def tearDown(self):
    #    del self.student

    def test_initial_value_required_attributes(self):
        self.assertEqual(self.student.last_name, 'Duck')
        self.assertEqual(self.student.first_name, 'Daisy')
        self.assertEqual(self.student.major, 'AAS')
        #self.assertEqual(self.student.gpa, 4.0)

    """def test_inital_all_attributes(self):
        person = t.Person('Duck', 'Daisy', '111-11-1111') # this is not self.person from setUp, but local
        assert person.last_name == 'Duck'                 # note no self here on person or assert
        assert person.first_name == 'Daisy'
        assert person.ssn == '111-11-1111'

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            p = t.Person('123', 'Daisy')

    def test_object_not_created_error_fist_name(self):
        with self.assertRaises(ValueError):
            p = t.Person('Duck', '123')

    def test_object_not_created_error_ssn(self):
        with self.assertRaises(ValueError):
            p = t.Person('Duck', 'Daisy', 'abc')

    def test_person_class_display_name(self):
        self.assertEqual(str(self.person), "Duck, Daisy:")   # Uses person from setUp()

    def test_person_class_display_name_ssn(self):
        p = t.Person('Duck', 'Daisy', '111-11-1111')    # Does not use person from setUp(), has local p
        self.assertEqual(str(p), "Duck, Daisy:111-11-1111")

    def test_person_str(self):
        self.assertEqual(str(self.person), 'Duck, Daisy:')'''

"""
if __name__ == '__main__':
    unittest.main()
