"""10-9 Silent Cats and Dogs
Modify your except block in Exercise 10-8 to fail silently if either file is missing."""

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
    pass