"""Øvelse med if-elif-else statement
NB: HDet ville reelt være mere oplagt med et if-elif-elif statement sådan at kun gyldige farver kunne give point"""

#Test hvor if-delen kører
alien_color = "green"

if alien_color == "green":
    points = 5
elif alien_color == "yellow":
    points = 10
else:
    points = 15

print("\nYou just scored " + str(points) + " points!")


#Test hvor elif-delen kører
alien_color = "yellow"

if alien_color == "green":
    points = 5
elif alien_color == "yellow":
    points = 10
else:
    points = 15

print("\nYou just scored " + str(points) + " points!")


#Test hvor else-delen kører
alien_color = "red"

if alien_color == "green":
    points = 5
elif alien_color == "yellow":
    points = 10
else:
    points = 15

print("\nYou just scored " + str(points) + " points!")