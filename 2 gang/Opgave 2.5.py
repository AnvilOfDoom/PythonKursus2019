#lister med tal

"""
#Oprindeligt forsøg
list_ten = range(1,11)
print(type(list_ten))


for value in list_ten:
    print(value)

#liste med 3-tabellen
list_three = range(3,100,3)

for value in list_three:
    print(value)
"""


"""liste med tallene 1-10. Hvis jeg ville kunne udskrive listen som liste, hvor den faktisk giver det rigtige
så burde jeg bruge list(range(x, x))"""

list_ten = list(range(1,11))
for value in list_ten:
    print(value)

#liste med 3-tabellen
list_three = list(range(3,100,3))
for value in list_three:
    print(value)
