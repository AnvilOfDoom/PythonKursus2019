#andre operationer på lister
list_three = list(range(3,100,3))

#mindste værdi
print(min(list_three))

#største værdi
print(max(list_three))

#sum
print(sum(list_three))

#gennemsnit
antal = len(list_three)

gennemsnit = sum(list_three)/antal
print(gennemsnit)

#alternativ m. gennemsnit
count = 0

for value in list_three:
    count +=1

sum_of_three = sum(list_three) / count
print(sum_of_three)