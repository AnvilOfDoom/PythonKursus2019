"""7-4. Pizza Toppings
A loop that prompts the user to pizza toppings until they enter 'quit'. For each topping write that it will be added."""

#a flag to make the while statement keep running until the flag is changed.
active = True

#loop that runs as long as active remains true, first asks for a topping, then checks if the topping is quit,
#in which case active changes to False and the loop ends. Otherwise it will print the topping and then ask again.
while active:
    choose_toppings = input("Please enter a topping, write 'quit' when done: ")
    if choose_toppings == "quit":
        active = False
    else:
        print(choose_toppings)
