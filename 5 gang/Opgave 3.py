"""Opgave 3
Lav en ny funktion som har samme funktionalitet som funktionen i opgave 3,
men denne gang skal den ikke returnere noget,
men den skal modificere listen I SELVE FUNKTIONEN således at summen af tallet bliver sat ind til sidst i listen.

Så f.eks. ved et input på [1,2,3], så skal listen modificeres til nu at indeholde [1,2,3,6].

Så prøv at teste dette ved at printe listen ud før og efter funktionskaldet
- så skal du kunne se forskel på elementerne der bliver udskrevet i de to prints().
Ville det være muligt at sende en parameter (altså en liste) til denne funktion
(som jo modificerer en listen) UDw3EN at vores liste faktisk bliver ændret?
"""

talliste = [1, 2, 3, 4, 5]
print(talliste)

def sum_liste_ii(liste):
    """Lægger tallene i input-listen sammen og returnerer summen"""
    output_liste = 0
    for tal in liste:
        output_liste += tal
    liste.append(output_liste)

sum_liste_ii(talliste)
print(talliste)

#Kald af funktionen med en kopi, hvorfor listen faktisk ikke modificeres
sum_liste_ii(talliste[:])
print(talliste)