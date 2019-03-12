"""Opgave 4 - manuelt type check

Prøv følgende kode af i dit program:
[indsat nedenfor]
Hvad kan du observere?
"""
# Koden nedenfor tjekker om en instance er et eksempel på en class/child class og giver
# en True/False værdi tilbage. En instance tæller både som et eksempel på den child class
# den er fra og som et eksempel på den parent class, dens child class arver fra
# men selvfølgelig ikke som et eksempel på andre child classes

import klasser as k

print("")
#bog
bog1 = k.Bog(1, "Ringenes Herre: Eventyret om Ringen", 1954, 423, "J.R.R. Tolkien",)
#lotr.tostring()


print("")
#film
film1 = k.Film(2, "Captain America: The First Avenger", 2011, "Joe Johnston", 124)
#capa.tostring()


if isinstance(bog1, k.Bog):
   print("bog1 er en Bog")
else:
   print("bog1 er ikke en Bog")

if isinstance(film1,k.Film):
   print("film1 er en Film")
else:
   print("film1 er ikke en film")

if isinstance(film1,k.Materiale):
   print("film1 er Materiale")
else:
   print("film1 er ikke Materiale")

if isinstance(film1,k.Bog):
   print("film1 er en Bog")
else:
   print("film1 er ikke en Bog")
