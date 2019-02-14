"""6-10. Favorite Numbers
Modifying 6-2 so each person have more favourite numbers."""

#dictionary of people and their favorite numbers
favorite_numbers = {"Emil": [1], "Rose": [3], "Mike": [7, 42], "Kaleb": [15, 42], "Denis": [31]}

#printing the keys and values of the dictionary.
for name, numbers in favorite_numbers.items():
    print(name + "'s favorite number(s) is/are: ")
    for number in numbers:
        print(number)