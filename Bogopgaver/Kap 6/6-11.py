"""6-11. Cities
A dictionary of dictionaries, one dictionary each per city, which then contains info about that city"""

#Dictionary of cities
cities = {
    "aarhus": {"country": "denmark", "population": 273000, "current mayor": "jacob bundsgaard"},
    "copenhagen": {"country": "denmark", "population": 613000, "current mayor": "frank jensen"},
    "aalborg": {"country": "denmark", "population": 137000, "current mayor": "thomas kastrup-larsen"},
    }

for city, city_information in cities.items():
    print(
        city.title() + " is a city in " +
        city_information["country"].title() +
        " with a population of around " +
        str(city_information["population"]) + " people." +
        " The current mayor is called " + city_information["current mayor"].title() + ".\n")









