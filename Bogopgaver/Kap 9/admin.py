"""Has the classes Admin and Privileges"""

from users_2 import Users

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

class Admin(Users):
    """This class is used for admin users"""
    def __init__(self, first_name, last_name, user_name, age):
        """initializes an admin"""
        super().__init__(first_name, last_name, user_name, age)
        self.privileges = Privileges()