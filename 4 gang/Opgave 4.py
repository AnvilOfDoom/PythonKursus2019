"""Brugerinput og dictionaries
Opbyg dansk - engelsk ordbog vha dictionaries og input.
- Dvs. brugeren skal kunne indtaste både danske ord og de engelske oversættelser.
- Det indtastede skal så gemmes i ens dictionary.
- Man skal kunne forlade programmet ved at taste q.
- udskriv ordbogen når man er færdig"""

#tom ordbog, der er klar til input:
dk_en_ordbog = {}

#information om hvordan brugeren kan afslutte programmet:
print("Du kan taste 'q' for at afslutte indtastningen, når du ikke vil tilføje flere ord.")

#det faktiske while loop
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