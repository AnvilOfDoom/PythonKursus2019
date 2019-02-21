"""Brug af ordbogen
Bruger ordbogen fra opgave 4. Når ordbogen er lavet, så skal der være et nyt program, der beder en
indtaste et søgeord, som vil have oversat til engelsk. Når brugeren har indtastet sit ord, så søger programmet
i dictionary efter det og printer så oversættelsen.
Hvis ordet ikke findes i ordbogen, så skal programmet skrive dette.
Igen skal q lade brugeren afslutte."""

#tom ordbog, der er klar til input:
dk_en_ordbog = {}

#information om hvordan brugeren kan afslutte programmet:
print("Du kan taste 'q' for at afslutte indtastningen, når du ikke vil tilføje flere ord.")

#det faktiske while loop, der opbygger ordbogen
while True:
    dansk = input("Indtast et dansk ord: ") #indtast det danske ord
    if dansk.lower() == "q":        #tjekker om brugeren vil afslutte
        break
    engelsk = input ("Indtast engelsk oversættelse: ")  #indtask engelsk oversættelse
    if engelsk.lower() == "q":      #tjekker om brugeren vil afslutte
        break
    dk_en_ordbog[dansk] = engelsk   #det indtastede ordpar bliver tilføjet til ordbogen.

for key, value in dk_en_ordbog.items(): #udskriver ordbogen
    print(key + ": " + value)

#Søgefunktion
print("Du får nu mulighed for at søge efter ord i ordbogen, sådan at oversættelsen slås op for dig. Tryk q når "
      "ikke skal bruge flere oversættelser.") #præsentation, fortæller også om exit kommando.

while True:
    search = input("Indtast et dansk ord, du vil have oversat til engelsk, hvis ordbogen har ordet, så får du "
               "oversættelsen tilbage: ")
    if search.lower() == "q":   #lukker programmet
        break
    else:
        for key, value in dk_en_ordbog.items():
            if search.lower() == key.lower():#tjekker om søgeordet findes i ordbogen. pga lower() case insensitive
                print("Ordet betyder: " + value.title())
                break
            else:
                print("Din søgning gav desværre intet resultat.") #søgningen gav intet resultat

