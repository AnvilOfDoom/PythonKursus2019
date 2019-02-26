"""Gør det følgende med en while-løkke i stedet.
for x in range(0,11):
   print(x)
"""
counter = 0

while counter <= 10:
    print(counter)
    counter += 1

print("##############")

"""Gør følgensde med en for-løkke i stedet:
tal = [20,30,40,50,60,70]
index = 0
while tal[index]<50:
   print(tal[index])
   index+=1
Denne stump kode vil skrive tallene 20, 30 og 40 ud.
"""

tal = [20,30,40,50,60,70]

for number in tal:
    if number < 50:     #udelukker tallene i listen, der er højere end 40
        print(number)



#eksperiment med uendelig for-løkke
sisyfos_arbejde = ["sisyfos", "sten"]

for string in sisyfos_arbejde:
    sisyfos_arbejde.append(string)
    print("uendelig løkke")
    print(len(sisyfos_arbejde)