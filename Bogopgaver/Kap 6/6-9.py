"""6-9. Favorite Places
Lists in dictionary"""

#divtionary with keys with one or more values associated to the one key
favorite_places = {
    "emil": ["athens"],
    "rikke": ["berlin", "copenhagen"],
    "gitte": ["copenhagen", "jutland", "london"],
    }

#printing all the locations of each person
for name, places in favorite_places.items():
    if len(places) == 1:
        print(name.title() + "'s favorite place is:")
        print(places[0].title())
    else:
        print("The favorite places of " + name.title() + " are the following:")
        for place in places:
            print(place.title())
    print("")

print("################\n")

#alternate soluation
for name, places in favorite_places.items():
    if len(places) == 1:
        print(name.title() + "'s favorite place is:")
    else:
        print(name.title() + "'s favorite places are:")
    for place in places:
        print(place.title())
    print("")
