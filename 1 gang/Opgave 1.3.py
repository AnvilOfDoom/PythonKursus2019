"""Dette er en test af simple matematiske operationer.
Til sidst prøver jeg ogås at lave en integer til en string"""

#test af addition
matemagisk = 7+5
print(matemagisk)

#test af subtraktion
matemagisk = 17-5
print(matemagisk)

#test af multiplikation
matemagisk = 3*4
print(matemagisk)

#test af division, hvis man bruger dobbelt skråstreg så forbliver datatypen en integer i stedet for at divisionen
#får den til at blive til en float. Specifikt smider den alt efter punktummet væk, så der er ingen afrunding.
matemagisk = 24/2
print(matemagisk)

#test af potens, her tre i tredje.
powertest = 3**3
print(powertest)

#test af om man kan lægge en integer til en float. Det kan man.
sum = matemagisk+2
print(sum)

#konvertering af tal til string
tal = 20
tilString = "Nu er tallet en string, se: " + str(tal)
print(tilString)