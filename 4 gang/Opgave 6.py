


#Lader brugeren generere dansk/engelsk ordbog

#tom dictionary, der er klar til input:
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

#engelsk-dansk ordbog genereres ud fra
en_dk_ordbog = {}
counter = 0

for dansk, engelsk in dk_en_ordbog.items():
    if engelsk not in en_dk_ordbog.keys():
        en_dk_ordbog[engelsk] = dansk

#Søgefunktion (søger i engelsk-dansk ordbog)
while True:
    search = input("Indtast et engelsk ord, du vil have oversat til dansk, hvis ordbogen har ordet, så får du "
               "oversættelsen tilbage. Tryk q når du ikke skal bruge flere oversættelser: ")
    if search.lower() == "q":   #lukker programmet
        break
    else:
        for key, value in en_dk_ordbog.items():
            if search.lower() == key.lower():#tjekker om søgeordet findes i ordbogen. pga lower() case insensitive
                print("Ordet betyder: " + value.title())
                break
            else:
                print("Din søgning gav desværre intet resultat.") #søgningen gav intet resultat