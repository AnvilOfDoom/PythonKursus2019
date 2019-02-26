"""Print af dictionaries med loops"""

#dictionary fra opgave 3.2:
navne = {"emil": "bøye",
         "morten": "hansen",
         "anders": "madsen",
         "søren": "svendsen",
         "kasper": "habbakuksen",
         }

#loop der udskriver både for- og efternavn:
for fornavn, efternavn in navne.items():
    print(fornavn.title() + " " + efternavn.title())

print("\n##############")
#loop der udskriver fornavnene
for fornavn in navne.keys():
    print(fornavn.title())

print("\n##############")
# loop der udskriver efternavnene
for efternavn in navne.values():
    print(efternavn.title())