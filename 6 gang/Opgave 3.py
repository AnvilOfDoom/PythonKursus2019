"""Opgave 3 - liste af forskellige typer af objekter.

Prøv følgende kode (husk at have din import og at have defineret et
bog objekt og et film objekt med navnene “bog1” og “film1” henholdsvis):
minListe = [bog1,film1] # definer en liste med de 2 objekter

for m in minListe:
   print(m.toString())
"""


import klasser as k

print("")
#bog
bog1 = k.Bog(1, "Ringenes Herre: Eventyret om Ringen", 1954, 423, "J.R.R. Tolkien",)
#lotr.toString()


print("")
#film
film1 = k.Film(2, "Captain America: The First Avenger", 2011, "Joe Johnston", 124)
#capa.toString()


print("")
minListe = [bog1,film1] # definer en liste med de 2 objekter

for m in minListe:
   print(m.toString())
