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