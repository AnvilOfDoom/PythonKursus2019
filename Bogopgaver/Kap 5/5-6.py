"""Endnu en øvelse med if-elif-else statements
NB: if-elif-elif uden else ville nok give mere mening egentlig, sådan at kun tal ville anerkendes"""

alder = 77

if alder < 2:
    livsstadium = "a baby"
elif alder < 4:
    livsstadium = "a toddler"
elif alder < 13:
    livsstadium = "a kid"
elif alder < 20:
    livsstadium = "a teenager"
elif alder < 65:
    livsstadium = "an adult"
else:
    livsstadium = "an elder"

print("You are " + livsstadium + "!")