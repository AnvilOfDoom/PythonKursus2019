"""7-9. No Pastrami
Use list of orders from 2-8. Add 'pastrami' to the list three times.
Add code that says the deli has run out of pastrami. Use a while loop  to remove all pastrami orders"""

#list of sandwich orders
sandwich_orders = ["bacon", "pastrami", "baked bean", "cheese", "pastrami", "pastrami"]

#list of finished orders
finished_sandwiches = []

#message the deli has no more pastrami
print("Sorry! We have run out of pastrami! All pastrami orders will be cancelled! \n")

#removing the pastrami using a while loop
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

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