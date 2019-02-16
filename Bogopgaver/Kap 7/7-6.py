"""7-6. Three Exits""
Write three versions of 7-4 or 7-5 that do each of following once:\
- condition test in the while statement to stop the loop\
- use active variable to control how long the loop runs\
- use break statement to exit the loop when user enters a 'quit' value."""

#loop that runs while some condition is true
print("Loop that runs while condition is true. \n")
count = 0

while count < 5:
    count += 1
    print(count)


#use active variable to control how long the loop runs
#My initial version of 7-4 already did this:
print("\nLoop using an active variable.")
active = True

while active:
    choose_toppings = input("Please enter a topping, write 'quit' when done: ")
    if choose_toppings == "quit":
        active = False
    else:
        print(choose_toppings)


#variation that uses "break" to stop the loop. I simply removed the active flag and replaced it with break in the
# #if-statement.
print("\nLoop stopping with break statement.")
while True:
    choose_toppings = input("Please enter a topping, write 'quit' when done: ")
    if choose_toppings == "quit":
        break
    else:
        print(choose_toppings)