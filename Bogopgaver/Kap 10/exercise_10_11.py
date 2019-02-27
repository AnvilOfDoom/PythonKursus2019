"""10-11 Favorite Number
Write a program that prompts for the user’s favorite number.
Use json.dump() to store this number in a file.
Write a separate program that reads in this value
and prints the message, “I know your favorite number! It’s _____.”"""

#this program is the first of the two.
import json #importing JSON

favorite_number = input("Please enter your favorite number: ")
filename = "favorite_number.json"

with open(filename, "w") as f: #creating the file
    json.dump(favorite_number, f)   #dumping the entered value into a json dump
