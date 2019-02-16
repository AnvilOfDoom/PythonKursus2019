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

print("")
#calling the function with keyword arguments
make_shirt(message="Your mom!", size=18)