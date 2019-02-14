"""6-6. Polling
Combining list and dictionary"""

#code from the book (the exercise asks you to use it)
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
    }

#list of people who should take a favorite languages poll.
should_poll = ["jen", "ken", "edward", "carl"]


#loop
for name in should_poll:
    if name in favorite_languages:
        print("Thank you, " + name.title() + ", for taking the poll.")
    else:
        print(name.title() + ", you should take the poll!")