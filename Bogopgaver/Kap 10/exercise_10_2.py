"""10-2. Learning C
You can use the replace() method to replace any word in a string with a different word. Here’s a quick example
showing how to replace 'dog' with 'cat' in a sentence:

#>>> message = "I really like dogs."
#>>> message.replace('dog', 'cat')
'I really like cats.'
Read in each line from the file you just created, learning_python.txt,
and replace the word Python with the name of another language, such as C. Print each modified line to the screen."""
#denne fil giver en advarsel, men jeg aner ikke hvorfor. Den gør det uanset hvilken kode der er i filen...

with open("learningpython.txt") as file_object:
    lines = file_object.readlines()

for line in lines:
    line = line.rstrip()
    print(line.replace("Python", "C"))