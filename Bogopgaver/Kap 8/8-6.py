"""8-6. City Names:
Write a function called city_country() that takes in the name of a city and its country. The function should return a
string formatted like this:

'Santiago, Chile'

Call your function with at least three city-country pairs, and print the value that’s returned."""

def city_country(city_name, country):
    """This function takes a city name and a country and prins a string with the two"""
    return(city_name.title() + ", " + country.title())

#calling the function
city = city_country("athens", "greece")
print(city)

city = city_country("constantinople", "roman empire")
print(city)

city = city_country("berlin", "germany")
print(city)