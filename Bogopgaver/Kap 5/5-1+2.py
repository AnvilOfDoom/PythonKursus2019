#5-1 Conditional Tests

#equality
language = "Doric Greek"
print("Is language == Doric Greek? I predict True.")
print(language == "Doric Greek")

print("Is language == Attic Greek? I predict False.")
print(language == "Attic Greek")

#inequality
print("Is language != Doric Greek? I predict False")
print(language != "Doric Greek")

print("Is language != Attic Greek? I predict True")
print(language != "Attic Greek")

#test using lower() function
#first test has no adjustment for case
print("Is language == attic greek? I Predict False")
print(language == "attic greek")

print("Is language == attic greek? I Predict False")
print(language.lower() == "attic greek")

print("Is language == doric greek? I Predict False")
print(language.lower() == "doric greek")

#numerical test, equality
age = 18

print("Is age = 18? I predict True")
print(age == 18)

print("Is age = 17? I predict False")
print(age == 17)

#numerical test, inequality
print("Is age != 17? I predict True")
print(age != 17)

print("Is age != 18? I predict False")
print(age != 18)

#numerical test greater than
print("Is 29 > age? I predict True")
print(29 > age)

print("Is 9 > age? I predict False")
print(9 > age)

#numerical test greater than or equal
print("Is 18 >= age? I predict True")
print(18 >= age)

print("Is 19 >= age? I predict True")
print(19 >= age)

print("Is 9 >= age? I predict False")
print(9 >= age)

#numerical test less than
print("Is 29 < age? I predict False")
print(29 > age)

print("Is 9 < age? I predict True")
print(9 > age)

#numerical test less than or equal
print("Is 18 <= age? I predict True")
print(18 <= age)

print("Is 19 <= age? I predict False")
print(19 <= age)

print("Is 9 <= age? I predict True")
print(9 <= age)

#test using and keyword
print("Is (18 = age) and (9 < age)? I predict True")
print((18 == age) and (9 < age))

print("Is (19 = age) and (9 < age)? I predict False")
print((19 == age) and (9 < age))

#test using or keyword
print("Is (19 = age) or (9 < age)? I predict True")
print((19 == age) or (9 < age))

print("Is (19 = age) or (29 < age)? I predict False")
print((19 == age) or (29 < age))

#test whether an item is in list
languages = ["Doric Greek", "Ionian Greek", "Attic Greek", "Persian", "Aramaic", "Egyptian", "Hittite"]

print("Is 'Doric Greek' in the list? I predict True")
print("Doric Greek" in languages)

print("Is 'Latin' in the list? I predict False")
print("Latin" in languages)

#test whether item is not in list
print("Is 'Doric Greek' not in the list? I predict False")
print("Doric Greek" not in languages)

print("Is 'Latin' not in the list? I predict True")
print("Latin" not in languages)

#test exclusive or (?)
print("Exclusive or? I predict False")
print(
        (("Doric Greek" not in languages) and ("Ionian Greek" in languages))
        or
        (("Doric Greek" in languages) and ("Ionian Greek" not in languages)))

print("Exclusive or? I predict True")
print(
        (("Doric Greek" not in languages) and ("Latin" in languages))
        or
        (("Doric Greek" in languages) and ("Latin" not in languages)))



