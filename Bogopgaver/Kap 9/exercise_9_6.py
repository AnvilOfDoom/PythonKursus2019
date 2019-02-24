"""9-6. Ice Cream Stand
An ice cream stand is a specific kind of restaurant.
Write a class called IceCreamStand that inherits from the Restaurant class you wrote in
Exercise 9-1 (page 166) or Exercise 9-4 (page 171).

Either version of the class will work; just pick the one you like better.
Add an attribute called flavors that stores a list of ice cream flavors.
Write a method that displays theese flavors.
Create an instance of IceCreamStand, and call this method."""

#Restaurant class from 9-1:
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

#subclass for ice cream stands
class IceCreamStand(Restaurant):
    """Represents ice cream stands as a subcategory of restaurants"""

    def __init__(self, restaurant_name, cuisine_type):
        """initializes attributes from parent class"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["chocolate", "vanilla", "mint"]

    def display_IceCreamFlavors(self):
        """Method to print a list of the flavors in the flavors list"""
        print(self.restaurant_name.title() + " carries the following flavors:")
        for flavor in self.flavors:
            print(flavor.title())

#creating ice cream stand and then printing the flavors.
paradis = IceCreamStand("paradis", "ice cream")
paradis.display_IceCreamFlavors()