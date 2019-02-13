"""6-2. Favorite Numbers
Exercise creating a dictionary of persons and their favorite numbers"""

#dictionary of people and their favorite numbers
favorite_numbers = {"Emil": 1, "Rose": 3, "Mike": 7, "Kaleb": 15, "Denis": 31}

#printing the keys and values of the dictionary.
for value in favorite_numbers:
    print(value + "'s favorite number is " + str(favorite_numbers[value]))