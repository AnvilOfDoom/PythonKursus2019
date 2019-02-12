#3-8 Seeing the World

#list of places I would like to visit
locations = ["Sevilla", "Canada", "Athens", "Mount Olympos", "Thebes"]
print(locations)

#printing it sorted alphateically
print(sorted(locations))

#print showing the order in the list itself has not been changed.
print(locations)

#printing it sorted in reverse alphabetical order
print(sorted(locations, reverse=True))

#print showing the order in the list itself has not been changed.
print(locations)

#actually reversing the order of the list
locations.reverse()
print(locations)

#restoring the original order by reversing it again
locations.reverse()
print(locations)

#changing order to alphabetical
locations.sort()
print(locations)

#changing order to reversed alphabetical
locations.sort(reverse=True)
print(locations)