"""9-14. Dice
The module random contains functions that generate random numbers in a variety of ways.
The function randint() returns an integer in the range you provide.
The following code returns a number between 1 and 6:

    from random import randint
    x = randint(1, 6)

Make a class Die with one attribute called sides, which has a default value of 6.
Write a method called roll_die() that prints a random number between 1 and the number of sides the die has.
Make a 6-sided die and roll it 10 times.
Make a 10-sided die and a 20-sided die.
Roll each die 10 times."""

#importing function from random
from random import randint

#making the Die class

class Die():
    def __init__(self, sides=6):
        """initializes die"""
        self.sides = sides

    def roll_die(self):
        """produces a number between 1 and the number of sides"""
        return randint(1, self.sides)

#creating a six-sided die
six = Die()

#rolling the die
print(six.roll_die())

print("")
#rolling it ten times
for value in range(1, 11):
    print(six.roll_die())

#creating a ten-sided die
ten = Die(sides=10)

print("")
#rolling it ten times
for value in range(1, 11):
    print(ten.roll_die())

#creating a ten-sided die
twenty = Die(sides=20)

print("")
#rolling it ten times
for value in range(1, 11):
    print(twenty.roll_die())