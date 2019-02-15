"""6-8. Pets
Another list with dictionaries, then printing everything known about each pet"""

#list of pets
pets = []


#dictionaries of pets, creating the pet dictionaries and appending them to the list

pet = {"name": "claw", "kind of animal": "cat", "owner's name": "laura"}
pets.append(pet)

pet = {"name": "drool", "kind of animal": "dog", "owner's name": "richard"}
pets.append(pet)

#printing the pets
for pet in pets:
    for key, value in pet.items():
        print(key.title() + ": " + value.title())
    print("")
