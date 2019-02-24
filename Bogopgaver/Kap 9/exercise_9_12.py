"""9-12. Multiple Modules
Store the User class in one module,
and store the Privileges and Admin classes in a separate module.
In a separate file, create an Admin instance
and call show_privileges() to show that everything is still working correctly."""

from admin import Admin

#creating an admin user
anvil = Admin("søren", "bøye", "anvil", 31)

#printing privileges
anvil.privileges.show_privileges()