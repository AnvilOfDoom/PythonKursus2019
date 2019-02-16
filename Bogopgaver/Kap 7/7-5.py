"""7-5. Movie Ticket
Create a loop that asks users their age and then prints the cost of their movie ticket depending on that age."""


#the loop asks for input, then converts the input to a string, then prints the relevant output.
#Notice that the loop never ends - unless the user enters input with anything that is not an integer.
while True:
    age = input("What is your age? ")
    age = int(age)
    if age < 3:
        print("Ticket is free.")
    elif age <= 12:
        print("Your ticket costs $10.")
    elif age > 12:
        print("Your ticket costs $15.")


