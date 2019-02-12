#modifikation
yndlingsforfattere = ["Tolkien", "Pullman", "Epikur", "Mill", "Nietzsche"]

for forfatter in yndlingsforfattere:
    print(forfatter)

#tilføjer forfatter til listen
yndlingsforfattere.append("Hume")
for forfatter in yndlingsforfattere:
    print(forfatter)

#fjerner nr. 2 fra listen

del yndlingsforfattere[1]
print(yndlingsforfattere)