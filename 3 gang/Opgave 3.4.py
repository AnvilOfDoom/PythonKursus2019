"""Samme dictionary som fra 3.2 og 3.3, tilføj et nyt key-value par og udskriv derefter dictionary igen for at se
det nye par er tilføjet. Derefter slettes første navnepar"""

#dictionary fra 3.2:
navne = {"emil": "bøye",
         "morten": "hansen",
         "anders": "madsen",
         "søren": "svendsen",
         "kasper": "habbakuksen",
         }

#tilføjer navnepar
navne["niels"] = "nielsen"

#print (samme loop som det første i 3.3)
for navn in navne.keys():
    print(navn.title() + " " + navne[navn].title())

#sletning af første navnepar med del
del navne["emil"]

#print for at bekræfte sletning
print("\n##############")
for navn in navne.keys():
    print(navn.title() + " " + navne[navn].title())

