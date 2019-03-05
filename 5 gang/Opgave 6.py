"""Opgave 6 - funktioner fra standardbiblioteket
Stort set alt i standard bibliotet er faktisk funktioner
(også nogle gange kaldt metoder eller methods på engelsk), som så virker på forskellige datatyper.

Prøv f.eks. at gå ind på denne side fra den officielle python documentation
https://docs.python.org/3.7/library/stdtypes.html#string-methods

Der er defineret de metoder som virker på strings - hvis du scroller lidt ned.
Læs documentation for følgende funktioner og lav nogle små program stumper som bruger disse funktioner:
strip
isdigit
join (hvor du skal bruge # som adskille tegn). Hvad skal input være?
"""

#strip
print("   aaabbbccc   ".strip()) #fjerner white space rundt om indholdet i den string, funktionen anvendes på.
print("   aaabbbccc   ".strip("a ")) #fjerner det/de angivne symboler fra venstre og højre, stopper når den
                                # rammer et tegn, der ikke er inkluderet i input.
print('www.example.com'.strip('cmowz.'))


#isdigit - input skal være en string der består af tal og kun tal
print("test".isdigit())
print("123".isdigit())
print("12.3".isdigit())
print("".isdigit())
print("#123".isdigit())

#join - input skal være en liste af strings
print("#".join(["This", "is", "a", "test"]))