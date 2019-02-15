"""5.11 Ordinal Numbers
An exercise about creating a list of numbers 1-9 and printing them with the appropriate suffix (st, nd, rd, th"""

numbers = list(range(1, 10))

for value in numbers:
    if value == 1:
        print("1st")
    elif value == 2:
        print("2nd")
    elif value == 3:
        print("3rd")
    else:
        print(str(value) + "th")