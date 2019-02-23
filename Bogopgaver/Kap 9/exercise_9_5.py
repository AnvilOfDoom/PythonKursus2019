"""9-5. Login Attempts
Add an attribute called login_attempts to your User class from Exercise 9-3 (page 166).
Write amehtod called increment_login_attempts() that increments the value of login_attempts by 1.
Write another method called reset_login_attempts() that resets the value of login_attempts to 0.

Make an instance of the User class and call increment_login_attempts() several times.
Print the value of login_attempts to make sure it was incremented properly,
and then call reset_login_attempts().
Print login_attempts again to make sure it was reset to 0."""

#User class from 9-3.
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

#creating a user
user_01 = Users("emil", "staugaard", "anvil", 31)

#incrementing login attempts twice and then printing the value
user_01.increment_login_attempts()
user_01.increment_login_attempts()
print(user_01.login_attempts)

#resetting the numer of login attempts and printing new value
user_01.reset_login_attempts()
print(user_01.login_attempts)