"""10-5. Programming Poll
Write a while loop that asks people why they like programming.
Each time someone enters a reason, add their reason to a file that stores all the responses."""

#variable for filename to use in program
filename = "programmingpoll.txt"

while True:
    response = input("Why do you like programming? ")    #asks for the user's name and saves to variable.
    if response == "q": #use this to exit the loop
        break
    else:
        with open(filename, "a") as file_object:
            file_object.write(response + "\n")