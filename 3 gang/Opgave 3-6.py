"""3-6. Søgning
Lav en liste over strenge (navne på lande). Derefter tjek om en søgestreng er i listen.
Fx søg efter 'mark' """

#liste over lande
lande = ["danmark", "tyskland", "storbritannien", "sverige", "holland"]

#søgeord
search = "land"

#søgning
for land in lande: #den kigger i hver værdi i listen
    if search in land: #søgestrengen defineres/refereres til.
        print("Succes! " + land.title() + " indeholder din søgning '" + search +"'")
        break # når break er her, så stopper den når den når første resultat.
    else: #hvis søgestrengen ikke findes
        print("Desværre! " + land.title() + " indeholder desværre ikke din søgning '" + search + "'")

print("\n##############################\n")
#ny opgave hvor vi laver en liste over alle søgeresultater på søgningen.
search_results = [] #tom liste til søgeresultater

for land in lande: #den kigger i hver værdi i listen
    if search in land: #søgestrengen defineres/refereres til.
        print("Succes! " + land.title() + " indeholder din søgning '" + search +"'")
        search_results.append(land) #tilføjer det positive resultat til listen over resultater.
    else: #hvis søgestrengen ikke findes
        print("Desværre! " + land.title() + " indeholder desværre ikke din søgning '" + search + "'")

antal_resultater = len(search_results)

print("\nDin søgning gav " + str(antal_resultater) + " resultater:")
for land in search_results:
    print(land.title())
