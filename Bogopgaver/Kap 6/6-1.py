"""6-1. Person
Exercise in creating a dictionary about a person you know"""

#dictionary with the following keys: first name, last name, age, and city.
person = {
    "first_name": "Emil",
    "last_name": "Hansen",
    "age": 33,
    "city": "Aarhus",
    }

#printing the values of the dictionary.
for characteristic in person:
    print(person[characteristic])