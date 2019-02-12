#3-10 Every Function

languages = ["Doric Greek", "Ionian Greek", "Attic Greek", "Persian", "Aramaic", "Egyptian", "Hittite"]
print(languages)

#print one e.g. print(languages[2])
print(languages[2])

#languages.append
languages.append("Latin")
print(languages)

#languages.insert(0)
languages.insert(0, "Phoenician")
print(languages)

#del languages[0]
del languages[0]
print(languages)

#languages.pop()
popped_language = languages.pop()
print(languages)
print(popped_language)

#languages.pop(0)
popped_language = languages.pop(0)
print(languages)
print(popped_language)

#languages.remove("value")
languages.remove("Aramaic")
print(languages)

#languages.sort()
languages.sort()
print(languages)

#languages.reverse()
languages.reverse()
print(languages)

#sorted(languages)
print(sorted(languages))

#len(languages)
print(len(languages))