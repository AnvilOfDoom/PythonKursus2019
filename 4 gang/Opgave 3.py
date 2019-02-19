"""Pakkeliste via brugerinput
Programmet skal:
- Spørge om brugeren ønsker at pakke en række ting fra en liste.
- Udskrive den endelige pakkeliste når du er færdig
- Automatisk afslutte og udskrive pakkelisten når du har valgt 5 objekter
- Tillade brugeren selv at afslutte når vedkommende ønsker det."""

#mulige ting at pakke
pakkeliste = ["tandbørste", "tandpasta", "pung", "pas", "oplader", "telefon", "bog", "briller"]

#endelig pakkelisten, tom i udgangspunktet
pakkeliste_done = []

#while-loop til at have det faktiske program.
print("Du kan taste 'q' for at afslutte pakningen, når du ikke vil pakke mere.")
while True:
    for ting in pakkeliste:
        pakkestatus = input("Ønsker du at pakke følgende ting: " + ting + "? y/n ")     #spørger om objekt skal pakkes
        if pakkestatus.lower() == "q":
            break
        elif pakkestatus == "y":
            pakkeliste_done.append(ting)#tilføjer den pakkede ting til listen over pakkede ting.
            #pakkeliste.remove(ting)     #fjerner den pakkede ting fra pakkelisten - dette giver problemer!
        if len(pakkeliste_done) == 5:    #tjekker om tasken er fuld, hvis den er det afsluttes programmet.
            print("Din taske er fuld! Program afsluttes!")
            break
    break


print("Du har pakket følgende ting:")
for objekt in pakkeliste_done:
    print(objekt.title())