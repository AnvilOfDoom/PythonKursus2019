def kvadrat(x: float)-> str:
    return str(x**2)

print("Resultatet er " + kvadrat(5))


print("")
print("#########################")
print("")

from typing import List

def minsum(liste : List[int]) -> str:
    sum_af_liste = 0
    for x in liste:
        sum_af_liste += x
    return str(sum_af_liste)

talliste = [1, 2, 3, 4]
print("Summen af min liste er " + minsum(talliste))

###
liste2 = ["anders","martin","benny"]
print("summen er : "+minsum(liste2)) #denne markeres med en advarsel fordi funktionen forventer en liste af integers.