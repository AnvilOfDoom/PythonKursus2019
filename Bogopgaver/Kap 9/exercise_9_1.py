"""9-1. Restaurant
Make a class called Restaurant. The __init__() method for Restaurant should store two attributes:
a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of information,
and a method called open_restaurant() that prints a message indicating that the restaurant is open.

Make an instance called restaurant from your class.
Print the two attributes individually, and then call both methods."""

class Restaurant():
    """This class is used to create restarant of a certain type."""

    def __init__(self, restaurant_name, cuisine_type):
        """Contains the name and type of the restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """this method describes the method, printing a message with name and the type of cuisine"""
        print(self.restaurant_name.title() + " is a " + self.cuisine_type + " restaurant.")

    def open_restaurant(self):
        """"simulates opening the restaurant"""
        print(self.restaurant_name.title() + " is now open!")

#creating an instance of the class
china_star = Restaurant("china star grill", "fast food")


#printing the name
print(china_star.restaurant_name.title())

#printing the cuisine type
print(china_star.cuisine_type.title())

#describe the restaurant
china_star.describe_restaurant()

#open the restaurant
china_star.open_restaurant()