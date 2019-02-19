"""Opgave 7-5 fra bogen
Lav et loop der beder om brugerens alder og så oplever prisen for deres aldersgruåppe, hvorefter den spørger igen"""

#prisliste
price_infant = "is free!"
price_child = "costs $10."
price_adult = "costs $15."

while True:
    age = input("What is your age? Press q to stop: ")
    if age == "q":
        break
    elif int(age) < 3:
        print("Your ticket " + price_infant)
    elif int(age) < 13:
        print("Your ticket " + price_child)
    else:
        print("Your ticket " + price_adult)