"""6-5. Rivers
Exercise about creation a dictionary containing three major rivers and the country the river runs through."""

#dictionary
rivers = {"nile": "egypt", "rhine": "germany", "sepik": "new guinea"}


print("\n#############################\n")
#print of sentence about each river.
for river, country in rivers.items():
    print("The " + river.title() + " runs through " + country.title() + ".")


print("\n#############################\n")
#print af keys, dvs. flodernes navne
for key in rivers:
    print(key.title())


print("\n#############################\n")
#print af values, dvs. flodernes lande.
for value in rivers:
    print(rivers[value].title())