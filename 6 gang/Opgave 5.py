import klasser as k
bog1 = k.Bog(1, "Ringenes Herre: Eventyret om Ringen", 1954, 423, "J.R.R. Tolkien",)
film1 = k.Film(2, "Captain America: The First Avenger", 2011, "Joe Johnston", 124)

#test af kan udlåne
print(bog1.kanUdlaane())

bog1.udlaan() #udlåner en

print(bog1.kanUdlaane()) #tester igen for om der kan udlånes. Det kan der ikke længere


print("\n#############################\n")
#test af søgning
if bog1.matchTitle("Ringenes"):
    print("Din søgning er i titlen")
else:
    print("Din søgning matchede ikke titlen")

print("\n#############################\n")

if film1.matchTitle("Ringenes"):
    print("Din søgning er i titlen")
else:
    print("Din søgning matchede ikke titlen")