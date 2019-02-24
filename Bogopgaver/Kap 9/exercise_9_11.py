"""9-10. Imported Admin
Start with your work from Exercise 9-8 (page 178).
Store the classes User, Privileges and Admin in one module.
Create a separate file, make an Admin instance,
and call show_priveleges() to show that everything is working correctly."""

#importing the class
from users import Admin

#creating an admin user
anvil = Admin("søren", "bøye", "anvil", 31)

#printing privileges
anvil.privileges.show_privileges()