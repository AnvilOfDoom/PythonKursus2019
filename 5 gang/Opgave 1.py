###### hvis der er tid, så spørg Martin til unittest.main()


"""Opgave 1 - definition af en funktion med 2 parametre
Lav opgave 8-3 og  8-5 på side 141 i bogen.
"""

"""8-3. T-Shirt
Write function make_shirt() that uses a size and the text message to be written on the shirt.
Function should print a sentence summarizing the size and quoting the message.

Call function with positional arguments and then again with keyword arguments"""

#defining function using two parameters
def make_shirt(size, message):
    """This function creates a sentence about a t-shirt of a size and with a message provided via the parameters."""
    print("Making a size " + str(size) + " t-shirt with the following quote: " + '"' + message + '"')

#calling the function with positional arguments
make_shirt(18, "Your mom!")

#calling the function with keyword arguments
make_shirt(message="Your mom!", size=18)

print("")
"""8-5. Cities
Write function describe_city with two parameters: name and country. Function should print sentence with both parameters.
Parameter for country should have default value.
Call function for three cities, one of which should not be in default country"""

#defining the function
def describe_city(name, country = "denmark"):
    """This function prints a city and its country, both provided via the parameters. One parameter has a default value
    which is used if another is not specified in the function call."""
    print(name.title() + " is a city in " + country.title())

#call #1
describe_city("aarhus")

#call #2
describe_city("berlin", "germany")

#call #3
describe_city(country = "germany", name = "hamburg")