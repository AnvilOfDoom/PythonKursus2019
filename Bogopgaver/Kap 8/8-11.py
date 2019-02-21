"""Start with your work from Exercise 8-10. Call the function make_great() with a copy of the
list of magicians’ names. Because the original list will be unchanged, return the new list and
store it in a separate list. Call show_magicians() with each list to show that you have one list
of the original names and one list with the Great added to each magician’s name."""

#list of magicians
magician_names = ["gandalf", "saruman", "harry potter", "james randi"]


#function to add "the great" to each magician in  the list
def make_great(magicians):
    """adds 'the great' to the magicians by temporarily creating a new list and in that process modifying the values"""
    great_magicians = []
    while magicians:
        magician = magicians.pop() + " the great"
        great_magicians.append(magician)
    return great_magicians

#calling the function - improve by defining variables with the function and using the "show magicians" function
print(make_great(magician_names[:]))
print(magician_names)