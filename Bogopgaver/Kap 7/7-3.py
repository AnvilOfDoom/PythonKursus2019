"""7-3. Multiples of Ten
Ask for number and then report whether the number is a multiple of 10"""

#prompt for input
number = input("Please type a number and we will tell you if it is a multiple of 10: ")

#making the program interpret the input as an integer
number = int(number)

#check if it a multiple of 10, here done with an equality check
print(number % 10 == 0)

#Using the above check to print a more natural response
if number % 10 == 0:
    print("Yes, " + str(number) + " is a multiple of 10!")
else:
    print("No, " + str(number) + " is not a multiple of 10!")
