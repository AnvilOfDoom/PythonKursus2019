"""9-8. Privileges
Write a separate Privileges class.
The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance as an attribute in the Admin class.
Create a new instance of Admin and use your method to show its privileges."""

class Privileges():
    """A class for storing privileges"""
    def __init__(self):
        """initializes privileges"""
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """Method to print the privileges of the admin user"""
        print("This user has the following privileges:")
        for privilege in self.privileges:
            print(privilege.title())

#User class and Admin class from 9-7
class Users():
    """This class is used to create user profiles"""

    def __init__(self, first_name, last_name, user_name, age):
        "initializes a user"
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.age = age
        self.login_attempts = 0 #new attribute

    def summarize_user(self):
        """"prints a list of all attributes of the user"""
        print("User name: " + self.user_name)
        print("First name: " + self.first_name.title())
        print("Last name: " + self.last_name.title())
        print("Age: " + str(self.age))

    def greet_user(self):
        """prints a greeting for the user"""
        print("Welcome back, " + self.user_name +"!")

    def increment_login_attempts(self): #new method to count login attempts
        """Adds 1 to login_attempts"""
        self.login_attempts += 1

    def reset_login_attempts(self): #new method to reset login attempts
        """Sets login attempts to 0"""
        self.login_attempts = 0

class Admin(Users):
    """This class is used for admin users"""
    def __init__(self, first_name, last_name, user_name, age):
        """initializes an admin"""
        super().__init__(first_name, last_name, user_name, age)
        self.privileges = Privileges()  #this attribute now calls the Privileges class.

#creating user and then printing privileges
anvil = Admin("søren", "bøye", "anvil", 31)
anvil.privileges.show_privileges()
