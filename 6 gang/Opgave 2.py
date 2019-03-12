import klasser as k

#materiale
materialetest = k.Materiale(1, "testmateriale", 0000)
materialetest.tostring()


print("")
#bog
lotr = k.Bog(1, "Ringenes Herre: Eventyret om Ringen", 1954, 423, "J.R.R. Tolkien")
lotr.tostring()


print("")
#film
capa = k.Film(2, "Captain America: The First Avenger", 2011, "Joe Johnston", 124)
capa.tostring()