"""7-10. Dream Vacation
Create a poll for people to enter their name and dream vacation and then print the results."""

#an empty dictionary to contain the responses.
dream_vacations = {}

#active flag
active = True

#the poll loop

while active:
    #first getting the user to enter their name and dream vacation.
    name = input("Please enter your name: ")
    vacation = input("Please enter the destination of your dream vacation: ")

    #adding the reponses to the dictionary, using name as the key and the location as value.
    dream_vacations[name] = vacation

    #asking if the poll should continue, note that any answer other than no, No, NO, or nO will result in continuing
    repeat = input("Do you want to continue the poll? Yes/no: ")

    #if check to react to user input regarding repeat
    if repeat.lower().strip() == "no":
        active = False

#printing the poll results
for name, vacation in dream_vacations.items():
    print(name.title() + "'s dream vacation goes to: " + vacation.title() +".")


