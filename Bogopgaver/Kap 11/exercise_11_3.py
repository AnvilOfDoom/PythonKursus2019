""""11-3: Employee
Write a class called Employee.
The __init__() method should take in a first name, a last name,
and an annual salary, and store each of these as attributes.
Write a method called give_raise() that adds $5000 to the annual salary by default
but also accepts a different raise amount.

Write a test case for Employee.
Write two test methods, test_give_default_raise() and test_give_custom_raise().
Use the setUp() method so you don’t have to create a new employee instance in each test method.
Run your test case, and make sure both tests pass."""

class Employee():
    """Collects information about an employee's first and last names as well as their salary"""

    def __init__(self, first_name, last_name, annual_salary):
        """initialize employee"""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        """Increases salary by 5000 or by specified amount"""
        self.annual_salary += amount
"""
employee1 = Employee("Svend", "Eriksen", 1000)

print(employee1.first_name)
print(employee1.last_name)
print(employee1.annual_salary)

employee1.give_raise()
print(employee1.annual_salary)

employee1.give_raise(1000)
print(employee1.annual_salary)"""