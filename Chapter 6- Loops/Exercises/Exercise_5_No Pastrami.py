## Solutions for Chapter 6: Loops

# Exercise 5: No Pastrami
# Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times.

sandwich_orders = [
    'Mortadella', 'Pastrami', 'Ham and Cheese', 'Pastrami', 
    'Pita', 'Grilled Cheese', 'Pastrami']
finished_sandwiches = []

# Removing Pastrami:
print("\n\033[1;31m I'm sorry, the deli ran out of pastrami :(\033[0m")
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

# Sandwich Orders:
print("\n\033[1;33m ===================== \n  Sandwich Orders: 🥪  \n\033[1;33m ===================== \033[0m\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"> I made your {current_sandwich} sandwich")
    finished_sandwiches.append(current_sandwich)

# Finished Sandwiches:
print("\n\033[1;32m ========================= \n  \033[1mFinished Sandwiches: 🥪 \033[0m\n\033[1;32m ========================= \033[0m\n")
for sandwich in finished_sandwiches:
    print(f"> {sandwich} sandwich is done!")
print()