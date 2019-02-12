#kopiering af liste
yndlingsforfattere = ["Tolkien", "Pullman", "Epikur", "Mill", "Nietzsche"]

#kopi fra underviser, eksemplet illustrerer at man ikke kan kopiere en variabel med at sætte lighedstegn
# mellem en ny variabel og en gammel variabel, da det betyder de begge påvirkes af ændringer af en af dem.
kopi = yndlingsforfattere
kopi.append("Dostojevski")
print(kopi)
print(yndlingsforfattere)

#korrekt kopiering, vha slice

kopi = yndlingsforfattere[:]
kopi.append("Tolstoy")
print(kopi)
print(yndlingsforfattere)