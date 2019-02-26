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

#alternativ udgave af programmet hvor brugeren spørges til hvor meget der er plads til i deres taske
#kunne erstatte input() med en værdi, fx 5 og så vil det virke med den faste grænse på 5 objekter.
plads = input("Indtast venligst hvor mange genstande din taske har plads til: ")

print("Du kan taste 'q' for at afslutte pakningen, når du ikke vil pakke mere.")
while True:
    for ting in pakkeliste:
        pakkestatus = input("Ønsker du at pakke følgende ting: " + ting + "? y/n ")     #spørger om objekt skal pakkes
        if pakkestatus.lower() == "q":
            break
        elif pakkestatus == "y":
            pakkeliste_done.append(ting)#tilføjer den pakkede ting til listen over pakkede ting.
        if len(pakkeliste_done) == int(plads):    #tjekker om tasken er fuld, hvis den er det afsluttes programmet.
            print("Din taske er fuld! Program afsluttes!")
            break
    break

print("\nDu har pakket følgende ting:")
for objekt in pakkeliste_done:
    print(objekt.title())