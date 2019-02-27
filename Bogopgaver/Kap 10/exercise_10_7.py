"""10-7.
Wrap your code from Exercise 10-6 in a while loop
so the user can continue entering numbers
even if they make a mistake and enter text instead of a number."""

print("This program lets you enter two numbers one after the other "
      "and will then give you the sum of the numbers combined.")
while True:
    try:
        first_number = input("Please enter the first number: ")    #The first number
        if first_number == "q":
            break
        else:
            first_number = int(first_number)
        second_number = input("Please enter the second number: ")  # The second number
        if second_number == "q":
            break
        else:
            second_number = int(second_number)
    except ValueError:
        print("Please enter a number with no decimals.")
    else:
        result = first_number + second_number
        print(result)