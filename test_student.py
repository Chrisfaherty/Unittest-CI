import unittest
from student import student

class TestStudent(unittest.Testcase):


    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    def setUp(self):
        print('setUp')
        self.student = Student('John', 'Doe')


    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')


    def tearDown(self):
        print('tearDown')


    def test_full_name(self):
        print('test_full_name')
        self.assertEqual(self.student.full_name, 'John Doe')
    

    def test_email(self):
        print('test_email')
        self.assertEqual(self.student.email, 'john.doe@gmail.com')


    def test_alert_santa(self):
        print('test_alert_santa')
        self.student.alert_santa()

        self.assertTrue(self.student.naughty_list)