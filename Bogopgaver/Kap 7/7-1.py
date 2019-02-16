"""7-1. Rental Car
Prompt the user for what type of rental car they would like and then print a message about that car."""

#prompt uding a variable and the input() function. The string in input() is the message the user gets before
#the program asks for input.
car_prompt = input("What type of car would you like to rent? ")

#printing a message about the car the user has entered.
print("Let me see if I can you a " + car_prompt.title())