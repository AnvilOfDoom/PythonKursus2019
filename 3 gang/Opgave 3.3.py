"""Print af dictionaries med loops"""

#dictionary fra opgave 3.2:
navne = {"emil": "bøye",
         "morten": "hansen",
         "anders": "madsen",
         "søren": "svendsen",
         "kasper": "habbakuksen",
         }

#loop der udskriver både for- og efternavn:
for navn in navne.keys():
    print(navn.title() + " " + navne[navn].title())

print("\n##############")
#loop der udskriver fornavnene
for navn in navne.keys():
    print(navn.title())

print("\n##############")
# loop der udskriver efternavnene
for navn in navne.keys():
    print(navne[navn].title())