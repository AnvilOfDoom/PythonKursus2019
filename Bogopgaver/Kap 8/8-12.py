"""8-12. Sandwiches
Write a function that accepts a list of items a person wants on a sandwich.
The function should have one parameter that collects as many items as the
function call provides, and it should print a summary of the sandiwch that
is being ordered. Call the function three tiems, using a different
number of arguments each time."""

def make_sandwich(*contents):
    sandwich = [] #empty list to contain the items entered in the function call.
    for item in contents: #tilføjer ingredienser til sandwich-listen
        sandwich.append(item)
    print("Your sandwich is finished, it contains:")
    for item in sandwich: #udskriver sandwiches ingredienser
        print(item.title())

make_sandwich("chicken")
print("") #tilføjer bare tom linje for at gøre læsning af output lettere.
make_sandwich("chicken", "bacon")
print("")
make_sandwich("chicken", "bacon", "lettuce")