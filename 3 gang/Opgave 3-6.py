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
        break # når break er her, så stopper den når den første resultat.
    else: #hvis søgestrengen ikke findes
        print("Desværre! " + land.title() + " indeholder desværre ikke din søgning '" + search + "'")