"""9-4. Number Served:
Start with your program from Exercise 9-1 (page 166).
Add an attribute called number_served with a default value of 0.
Create an instance called restaurant from this class.
Print the number of customers the restaurant has served,
and then change this value and print it again.

Add a method called set_number_served() that lets you set the number of customers that have been served.
Call this method with a new number and print the value again.

Add a method called increment_number_served() that lets you increment the number of customers who’ve been served.
Call this method with any number you like that could represent how many customers were served in,
say, a day of business."""

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


#creating a restaurant
china_star = Restaurant("china star grill", "fast food")

#printing the number served
print(china_star.number_served)

#changing the number of served customers and printing the number again
china_star.number_served = 5
print(china_star.number_served)

#changing the number served using set_number_served and printing the number again
china_star.set_number_served(10)
print(china_star.number_served)

#incrementing the number served with increment_number_served
china_star.increment_number_served(3)
print(china_star.number_served)