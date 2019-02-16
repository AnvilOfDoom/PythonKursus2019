"""7-2. Restaurant Seating
This program should ask for a number of people in a dinner group. If the number is more than 8 the program should
print a message that they'll have to wait for a table. Otherwise print a message that their table is ready"""

#prompt for input
guests_number = input("How many are in your group? Please type a number: ")

#converting the answer to an integer
guests_number = int(guests_number)

#an if-else statement that prints a message depending on whether there are 1-8 guests or more.
if guests_number <= 8:
    print("Your table is ready.")
elif guests_number > 8:
    print("Please wait for a table to be ready.")