"""10-8. Silent Cats and Dogs
Make two files, cats.txt and dogs.txt.
Store at least three names of cats in the first file and three names of dogs in the second file.
Write a program that tries to read these files and print the contents of the file to the screen.
Wrap your code ina try-except block to catch the FileNotFound error,
and print a friendly message if a file is missing.
Move one of the files to a different location on your system,
and make sure the code in the except block executes properly."""

#NB: En bedre løsning ville komme filerne i en liste og bruge et for-loop. Dette ville betyde at programmet ikke
#stopper ved den første fil, der mangler.
try:
    # opening the cats.txt file
    with open("cats.txt") as cats:
        print("The list of cats contains:")
        for cat in cats:    #printing the contents
            print(cat.strip().title())

    print("")

    #opening the dogs.txt file
    with open("dogs.txt") as dogs:
        print("The list of dogs contains:")
        for dog in dogs:    #printing the contents
            print(dog.strip().title())
except FileNotFoundError:
    print("One or more of your files are missing.")