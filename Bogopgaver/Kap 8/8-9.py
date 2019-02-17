"""8-9: Magicians
Make a list of magician’s names. Pass the list to a function called show_magicians(),
wich prints the name of each magician in the list."""

#list of magicians
magician_names = ["gandalf", "saruman", "harry potter", "james randi"]

def show_magicians(magicians):
    """function that expect a list and then prints the contents of the list one by one"""
    for magician in magicians:
        print(magician.title())

show_magicians(magician_names)