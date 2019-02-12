#4-10 Slices

languages = ["Doric Greek", "Ionian Greek", "Attic Greek", "Persian", "Aramaic", "Egyptian", "Hittite"]

#first three languages
print("The first three items on the list are:")
for language in languages[:3]:
    print(language)

#three middle languages
print("\nThree middle items on the list are:")
for language in languages[2:5]:
    print(language)

#last three languages
print("\nThe three last items on the list are:")
for language in languages[-3:]:
    print(language)