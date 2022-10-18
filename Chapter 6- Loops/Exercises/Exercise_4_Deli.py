## Solutions for Chapter 6: Loops

# Exercise 4: Deli
# Make a list called sandwich_orders and fill it with the names of various sandwiches.

sandwich_orders = ['Mortadella', 'Ham and Cheese', 'Pita', 'Grilled Cheese']
finished_sandwiches = []

# Sandwich Orders:
print("\n\033[1;33;40m ===================== \n  Sandwich Orders: 🥪  \n\033[1;33;40m ===================== \033[0m\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"> I made your {current_sandwich} sandwich")
    finished_sandwiches.append(current_sandwich)

# Finished Sandwiches:
print("\n\033[1;32;40m ========================= \n  \033[1mFinished Sandwiches: 🥪 \033[0m\n\033[1;32;40m ========================= \033[0m\n")
for sandwich in finished_sandwiches:
    print(f"> {sandwich} sandwich is done!")
print()