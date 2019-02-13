"""6-3. Glossary
Exercise for creating a dictionary with a glossary of programming terms."""

#the glossary
glossary_programming = {
    "string": "Data type. A string has a value that consists a sequence of characters (letters, numbers, etc) "
              "encapsulated in ''.",
    "integer": "Data type. Value consists of a number with no decimal fractions.E.g. 1.",
    "float": "Data  type. Value consists of a number with decimal fractions. E.g. 1.5.",
    "list": "A list of data, can contain string, integers, and floats.",
    "if-statement": "A statement that checks some condition, if the condition is true, a code block is run.",
    }

#printing the keys and values of the dictionary.
print("String: ".title() + glossary_programming["string"])
print("integer: ".title() + glossary_programming["integer"])
print("float: ".title() + glossary_programming["float"])
print("list: ".title() + glossary_programming["list"])
print("if-statement: ".title() + glossary_programming["if-statement"])