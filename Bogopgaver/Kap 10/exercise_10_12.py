"""10-12 Favorite Number Remembered
Combine the two programs from Exercise 10-11 into one file.
If the number is already stored, report the favorite number to the user.
If not, prompt for the user’s favorite number and store it in a file.
Run the program twice to see that it works."""

import json #importing JSON

filename = "favorite_number.json"

try:
    #loading number
    with open(filename) as f:
        favorite_number = json.load(f)
    print("Your favorite number is " + favorite_number +"!")
except FileNotFoundError:
    #saving number
    favorite_number = input("Please enter your favorite number: ")
    with open(filename, "w") as f: #creating the file
        json.dump(favorite_number, f)   #dumping the entered value into a json dump




