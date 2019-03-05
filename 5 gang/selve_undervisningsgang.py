#Underviseren viser i dag nogle ting, som ikke er i python 2, men som er i Python 3. De er derfor ikke i bogen,
# da den henvender sig til brugere af både 2 og 3.

#hvis man sender en liste ind i en funktion, så kan funktionen godt ændre dem.
#andre datatyper bliver ikke faktisk ændret af en funktion (normalt) (fx strenge, tal)

#ting fra Python 3:
#statisk typing:
def ret_linje_statisk(x: float) -> float:   #det efter pilen angiver at return-værdien skal være en float
    return 2*x + 1

print(ret_linje_statisk(2))
print(ret_linje_statisk(2.2))
print(ret_linje_statisk("bob")) #markeringen viser at den advarer mod en fejl, eftersom den ved der burde være en float.
