"""Øvelse med if-else statement"""

alien_color = "green"

#eksempel hvor "if"-delen kører
if alien_color == "green":
    points = 5
else:
    points = 10

print("You just scored " + str(points) + " points!")

#eksempeæ hvor "else"-delen kører
alien_color = "yellow"

if alien_color == "green":
    points = 5
else:
    points = 10

print("\nYou just scored " + str(points) + " points!")