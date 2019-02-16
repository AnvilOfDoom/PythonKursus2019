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




