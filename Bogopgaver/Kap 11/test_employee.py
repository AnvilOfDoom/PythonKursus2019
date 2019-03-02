import unittest
from exercise_11_3 import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the class Employee"""

    def test_give_default_raise(self):
        """Tests that give_raise with default value works"""