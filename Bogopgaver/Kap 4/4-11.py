#4-11 My Pizzas, Your Pizzas
pizzas = ["pepperoni", "vegetarian", "beef"]
friend_pizzas = pizzas[:]

pizzas.append("chicken")
friend_pizzas.append("moose")

print("My favourite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favourite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)