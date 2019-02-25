"""10-4. Guest Book
Write a while loop that prompts users for their name.
When they enter their name, print a greeting to the screen
and add a line recording their visit in a file called guest_book.txt.
Make sure each entry appears on a new line in the file."""

#variable for filename to use in program
filename = "guestbook.txt"

while True:
    name = input("Please write your name: ")    #asks for the user's name and saves to variable.
    if name == "q": #use this to exit the loop
        break
    else:
        with open(filename, "a") as file_object:
            print("Thank you for your visit, " + name.title() + ".")    #greeting
            file_object.write(name.title() + " visited.\n")
