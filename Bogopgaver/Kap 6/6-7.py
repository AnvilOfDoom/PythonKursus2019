"""6-7. People
Dictionaries in list. Starting with code from 6-1."""

#starting with code from 6-1
person_emil = {
    "first_name": "emil",
    "last_name": "hansen",
    "age": 33,
    "city": "aarhus",
    }

#additional people
person_mads = {
    "first_name": "mads",
    "last_name": "nielsen",
    "age": 14,
    "city": "aarhus",
    }

person_sara = {
    "first_name": "sara",
    "last_name": "jørgensen",
    "age": 37,
    "city": "aarhus",
    }


#list of people
people = [person_emil, person_mads, person_sara]


#printing the dictionaries for each person
"""for person in people:
    print(person)"""

for person in people:
    print(
        "First name: " + person["first_name"].title() +
        "\nLast name: " + person["last_name"].title() +
        "\nAge: " + str(person["age"]).title() +
        "\nCity: " + person["city"].title() + "\n"
        )







"""
#printing the values of the dictionary.
for person in people:
    print(person)
"""