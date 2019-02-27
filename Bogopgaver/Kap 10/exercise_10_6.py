"""10-6. Addition
One common problem when prompting for numerical input occurs when people provide text instead of numbers.
When you try to convert the input to an int, you’ll get a ValueError.
Write a program that prompts for two numbers.
Add them together and print the result.
Catch the TypeError if either input value is not a number,
and print a friendly error message.
Test your program by entering two numbers
and then by entering some text instead of a number."""

#prompting the user:
print("This program lets you enter two numbers one after the other "
      "and will then give you the sum of the numbers combined.")

try:
    first_number = int(input("Please enter the first number: "))    #The first number
    second_number = int(input("Please enter the second number: "))  # The second number
except ValueError:  #What to do in case of error
    print("Please enter a number with no decimals.")
else:
    result = first_number + second_number   #adding the numbers together
    print(result)   #printing the result