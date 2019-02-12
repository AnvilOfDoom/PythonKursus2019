"""Test af if-statements ud fra liste"""

favorite_fruits = ["apple", "pear", "banana"]

if "apple" in favorite_fruits:
    print("Sweet, sweet apples")

if "apple" in favorite_fruits:
    print("Sour, sour apples")

if "cinnamon bun" in favorite_fruits:
    print("It's not though....")

if "Banana".lower() in favorite_fruits:
    print("Checkmate atheists!")

if "banana".upper() in favorite_fruits:
    print("Don't shout!")