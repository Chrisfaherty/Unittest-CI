import unittest
from student import student

class TestStudent(unittest.Testcase):

    def test_full_name(self):
        student = Student('John', 'Doe')

        self.assertEqual(student.full_name, 'John Doe')
    

    def test_email(self):
        student = Student('John', 'Doe')

        self.assertEqual(student.email, 'john.doe@gmail.com')


    def test_alert_santa(self):
        student = Student('John', 'Doe')
        student.alert_santa()

        self.assertTrue(student.naughty_list)