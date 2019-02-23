"""9-1. Three Restaurants
Start with your class from Exercise 9-1. Create three different instances from the class,
and call describe_restaurant() for each instance."""

#class from 9-1
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

#creating three instances
china_star = Restaurant("china star grill", "fast food")
raadhuus_kafeen = Restaurant("raadhuus kafeen", "traditional Danish")
flammen = Restaurant("flammen", "meaty")

#describing the three restaurants.
china_star.describe_restaurant()
raadhuus_kafeen.describe_restaurant()
flammen.describe_restaurant()