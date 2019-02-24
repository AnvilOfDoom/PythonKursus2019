"""9-13. OrderedDict Rewrite
Start with Exercise 6-4 (page 108), where you used a standard dictionary to represent a glossary.
Rewrite the program using the OrderedDict class
and make sure the order of the output matches the order in which key-value pairs were added to the dictionary.

Note: In Python 3.6, dictionaries store keys in order.
However, this is not guaranteed to work in all versions of Python,
so you should still use an OrderedDict
when you need key-value pairs to be stored in a particular order."""

#importing the class:
from collections import OrderedDict

#the glossary
glossary_programming = OrderedDict()

#adding terms
glossary_programming["string"] = "Data type. A string has a value that consists a sequence of characters."
glossary_programming["integer"] = "Data type. Value consists of a number without a decimal point.E.g. 1."
glossary_programming["float"] = "Data  type. Value consists of a number with a decimal point. E.g. 1.5."

#printing the keys and values of the dictionary.
for danish, english in glossary_programming.items():
    print(danish + ": " + english)