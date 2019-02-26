"""Opgave 2
Lav en funktion som kan modtage en liste af tal og
så skal den vha af return returnere summen af de tal.
Du skal bruge en for løkke. F.eks. ved et input på [1,2,3] skal den returnere 6.
"""

talliste = [1, 2, 3, 4, 5]

#dum løsning
def sum_liste(liste):
    """funktion der tager med en liste og returnerer summen af listen"""
    return sum(liste)

print(sum_liste(talliste))


#løsning med for-løkke
def sum_liste_ii(liste):
    """Lægger tallene i input-listen sammen og returnerer summen"""
    output_liste = 0
    for tal in liste:
        output_liste += tal
    return output_liste

print(sum_liste_ii(talliste))


#alternativt

def sum_liste_iii(*tal):
    """funktion der tager mod et vilkårligt antal argumenter, laver en liste med dem og returnerer summen af listen"""
    talliste = []
    for number in tal:
        talliste.append(number)
    return(sum(talliste))

print(sum_liste_iii(1, 2, 3, 4, 5))