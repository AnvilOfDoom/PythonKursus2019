"""6-4. Glossary 2
Exercise for creating a dictionary with a glossary of programming terms.
This time printing with a loop"""

#the glossary
glossary_programming = {
    "string": "Data type. A string has a value that consists a sequence of characters (letters, numbers, etc) "
              "encapsulated in ''.",
    "integer": "Data type. Value consists of a number without a decimal point.E.g. 1.",
    "float": "Data  type. Value consists of a number with a decimal point. E.g. 1.5.",
    "list": "A list of data, can contain string, integers, and floats.",
    "if-statement": "A statement that checks some condition, if the condition is true, a code block is run.",
    "concatenating": "Combining strings using the + sign.",
    "tuple": "A type of list that cannot be changed (except by redefining it).",
    }

#printing the keys and values of the dictionary.
for term in glossary_programming.keys():
    print(term.title() + ": " + str(glossary_programming[term]))



