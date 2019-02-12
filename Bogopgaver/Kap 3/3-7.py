#3-6 Shrinking Guest List

guests = ["Hume", "Epicurus", "Nietzsche"]

print(guests[0] + " you are invied to dinner!")
print(guests[1] + " you are invied to dinner!")
print(guests[2] + " you are invied to dinner!")

print("\nWe have more guests!")

guests.insert(0, "Aurelius")
guests.insert(3, "Kim")
guests.append("Shapiro")

print("\n" + guests[0] + " you are invited to dinner!")
print(guests[1] + " you are invited to dinner!")
print(guests[2] + " you are invited to dinner!")
print(guests[3] + " you are invited to dinner!")
print(guests[4] + " you are invited to dinner!")
print(guests[5] + " you are invited to dinner!")

#announcing lack of places
print("\nSadly we only have room for two guests")

#removing guests one by one
popped_guests = guests.pop()
print("\nSorry, " + popped_guests + " we don't have roome for you after all!")

popped_guests = guests.pop()
print("\nSorry, " + popped_guests + " we don't have roome for you after all!")

popped_guests = guests.pop()
print("\nSorry, " + popped_guests + " we don't have roome for you after all!")

popped_guests = guests.pop()
print("\nSorry, " + popped_guests + " we don't have roome for you after all!")

#announcing remaining guests are still invited
print("\n" + guests[0] + " you are still invited to dinner!")
print(guests[1] + " you are still invited to dinner!")

#removing last names from list
del guests[0]
del guests[0]

print(guests)