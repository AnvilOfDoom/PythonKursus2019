"""7-8. Deli
Create a list of sandwich orders and an empty list for finished orders. The program should loop through the first list,
moving the order to the list of finished orders. Once all orders have been moved print a message listing each
sandwich that was made"""

#list of sandwich orders
sandwich_orders = ["bacon", "baked bean", "cheese"]

#list of finished orders
finished_sandwiches = []

#loop
while sandwich_orders:
    #removing an order from the list of orders - "making it"
    sandwich = sandwich_orders.pop()
    #message informing the sandwich has been made
    print("Your " + sandwich + " sandwich has been made.")
    #adding the sandwich to the list of finished sandwiches
    finished_sandwiches.append(sandwich)

print("")
#loop for printing the list of finished orders
for sandwich in finished_sandwiches:
    print("An order for " + sandwich + " sandwich has been completed.")
