"""9-7. Admin
An administrator is a special kind of user.
Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
or Exercise 9-5 (page 171).
Add an attribute, privileges, that stores a list of strings like
"can add post", "can delete post", "can ban user", and so on.
WRite a method called show_privileges() that lists the administrator’s set of privileges.
Create an instance of Admin, and call your method."""

#Users class from 9-5
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

#subclass for admin users

class Admin(Users):
    """This class is used for admin users"""
    def __init__(self, first_name, last_name, user_name, age):
        """initializes an admin"""
        super().__init__(first_name, last_name, user_name, age)
        self.privileges = ["can add post", "can delete post", "can ban user"]   #new attribute for admins

    def show_privileges(self):
        """Method to print the privileges of the admin user"""
        print("User " + self.user_name + " has the following privileges:")
        for privilege in self.privileges:
            print(privilege.title())

#creating user and then printing privileges
anvil = Admin("søren", "bøye", "anvil", 31)
anvil.show_privileges()
