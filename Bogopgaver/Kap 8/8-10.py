"""8-10. Great Magicians
Start with a copy of your program from Exercise 8-9. Write a function called make_great()
that modifies the list of magicians by adding the phrase the Great to each magician’s name.
Call show_magicians() to see that the list has actually been modified."""

#list of magicians
magician_names = ["gandalf", "saruman", "harry potter", "james randi"]


#function to add "the great" to each magician in  the list
def make_great(magicians):
    """adds 'the great' to the magicians by temporarily creating a new list and in that process modifying the values"""
    great_magicians = []
    while magicians:
        magician = magicians.pop() + " the great"
        great_magicians.append(magician)
    for great_magician in great_magicians:
        magicians.append(great_magician)
    return magicians

#calling the function
make_great(magician_names)
print(magician_names)



#function from 8-9
#def show_magicians(magicians):
#    """function that expect a list and then prints the contents of the list one by one"""
#    for magician in magicians:
#        print(magician.title())

#show_magicians(magician_names)