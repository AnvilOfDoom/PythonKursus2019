"""A module with the Restaurant class"""

class Restaurant():
    """This class is used to create restarant of a certain type."""

    def __init__(self, restaurant_name, cuisine_type):
        """Contains the name and type of the restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  #added attribute for counting the number of served customers.

    def describe_restaurant(self):
        """this method describes the method, printing a message with name and the type of cuisine"""
        print(self.restaurant_name.title() + " is a " + self.cuisine_type + " restaurant.")

    def open_restaurant(self):
        """"simulates opening the restaurant"""
        print(self.restaurant_name.title() + " is now open!")

    def set_number_served(self, customers): #new method
        """used to directly set the number of served customers"""
        self.number_served = customers

    def increment_number_served(self, customers): #new method
        """Add given number to number_served"""
        self.number_served += customers