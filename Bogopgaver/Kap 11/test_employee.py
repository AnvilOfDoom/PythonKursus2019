import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the class Employee"""
    def setUp(self):
        """creates an employee for use in test methods."""
        self.test_employee = Employee("John", "Doe", 1000)

    def test_give_default_raise(self):
        """Tests that give_raise with default value works"""
        self.test_employee.give_raise()
        self.assertEqual(self.test_employee.annual_salary, 6000)

    def test_give_custom_raise(self):
        """Tests that give_raise with custom value works"""
        self.test_employee.give_raise(1000)
        self.assertEqual(self.test_employee.annual_salary, 2000)

unittest.main()