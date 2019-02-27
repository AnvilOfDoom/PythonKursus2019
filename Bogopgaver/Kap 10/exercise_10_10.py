"""10-10. Common Words
Download a file from Project Gutenberg and count the number of times a word appears in teh work
use the count() method."""

with open("meslier.txt") as superstition:
    contents = superstition.read()              #actually reading the content into a variable
    print(contents.lower().count("abuse"))      #counting the word "abuse" and printing the result.
    print(contents.lower().count("malice"))
    print(contents.lower().count("superstition"))
    print(contents.lower().count("god"))
    print(contents.lower().count("priest"))
    print(contents.lower().count("evil"))
    print(contents.lower().count("tyrant"))

