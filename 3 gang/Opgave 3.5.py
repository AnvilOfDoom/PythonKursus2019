"""Nesting
Først en dictionary med navn på et land og en liste med landets tre største byer.
Dernæst endnu en dictionary med et andet land og dette lands tre største byer.
Til sidst en liste med de to dictionaries of et loop, der udskriver begge dictionaries."""

#dictionary for USA
usa = {"navn": "usa",
       "byer": ["new york city", "los angeles", "chicago"]}

#udskrift af usa
print(usa["navn"].upper() + "'s største byer er:")

    #for-loop der udskriver USA's største byer
for by in usa["byer"]:
    print("\t" + by.title())

#dictionary for Tyskland og udskrift heraf.
print("\n##############")
tyskland = {"navn": "tyskland",
       "byer": ["berlin", "hamburg", "münchen"]}

print(tyskland["navn"].title() + "s største byer er:")

    #for-loop der udskriver USA's største byer
for by in tyskland["byer"]:
    print("\t" + by.title())

print("\n##############")


#liste over lande-dictionaries og appending af dictionaries til listen
lande = []
lande.append(usa)
lande.append(tyskland)

print("\n##############")


#udskrift af lande-listen, inklusive if-else check så USA skrives all-caps og Tyskland med stort begyndelsesbogstav.
for land in lande:
    if land["navn"] == "usa":
        print(land["navn"].upper())
    else:
        print(land["navn"].title())
    for by in land["byer"]:
        print("\t" + by.title())
    print("")



