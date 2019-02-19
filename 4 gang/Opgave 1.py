"""Samme som opgave 7-1 og 7-2 i bogen
Dvs:
1) Bed om brugerinput med bestemt besked
2) Skriv et program der heder om input om hvor mange skal spise på en restaurant
Hvis svaret er over 8 skal de have én besked, ellers en anden."""

#7-1
user_input = input("What kind of car would you like? ") # definerer en variabel, der gemmer værdien af brugerens input
print("Let me see if I can find you a " + str(user_input))

#7-2
guests_number = input("How many people are in your group? Enter numer: ") # beder om brugerens input, gemmes i variabel

if int(guests_number) > 8:
    print("Please wait until a table is ready for you.")
else:
    print("Your table is ready!")