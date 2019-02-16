"""8-4. Large Shirts
Modifying the function from 8-3 so that there's a default value for size (L) and message has the default value of
'I love Python'
Make a large and a medium shirt with the default message and a shirt of any size with a different message."""

#defining function using two parameters, now with added default values
def make_shirt(size = "L", message = "I love Python"):
    """This function creates a t-shirt with a size and message provded via the parameters. Both parameters have default
    values in case none are provided by the function call"""
    print("Making a size " + str(size) + " t-shirt with the following quote: " + '"' + message + '"')

#making a large shirt with the default message. No need to define arguments.
make_shirt()

#making a medium shirt with the default message. Due the order of the values, size can be assigned with both position
# and with keyword.
make_shirt("M")

#making a large shirt with a different message. Here either use a keyword argument to modify the message or define both
#arguments in the function call.
make_shirt(message = "This is a different message")
make_shirt("L", "This is a different message")