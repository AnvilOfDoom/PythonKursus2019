"""9-10. Imported Restaurant
Using your latest Restaurant class, store it in a module.
Make a separate file that imports Restaurant.
Make a Restaurant instance,
and call one of Restaurant’s methods to show that the import statement is working properly."""

#importerer klassen
from restaurant import Restaurant

#laver en restaurant
china_star = Restaurant("china star grill", "fast food")

#kører method om restauranten
china_star.describe_restaurant()