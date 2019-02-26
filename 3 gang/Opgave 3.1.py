"""Konditionelle tests, eksempler"""

#Equality
print("Tjek for lighed".title())
print("Er værdien af filosof-variablen 'Aristoteles'? Vi gætter på ja.")

filosof = "Aristoteles"
#gæt
print(filosof == "Aristoteles")


#Inequality
print("\nTjek for ulighed".title())
print("Er værdien af filosof-variablen noget andet end 'Aristoteles'? Vi gætter  på nej")

print(filosof != "Aristoteles")


#Numerisk sammenligning, eksempel
print("\nSammenligning af tal (eksempel) - er 15 større end 17?")

alder_01 = 15
alder_02 = 17

print(alder_01 > alder_02)


#Tjek indhold af liste
print("\nEr Aristoteles blandt de største filosoffer?".title())
stoerste_filosoffer = ["Aristoteles", "Epikur", "Mill"]

print("Aristoteles" in stoerste_filosoffer)
print("Duh!")
