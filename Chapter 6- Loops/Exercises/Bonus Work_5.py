# Bonus Work #5: SOLO LEARN ACTIVITY (TICKET SYSTEM - WHILE LOOP) - 12/10/22
# Write a program that takes the ages of 5 passengers and outputs the total price for their tickets.

    ## ACTIVITY INSTRUCTIONS
# The price of a single ticket is $100.
# For children under 3 years of age, the ticket is free.

print("\n-----Ticketing System-----\n")
total = 0
ticket = 100
passengers = 1
while passengers <= 5: #while loop
    age = int(input("Enter age: "))
    passengers += 1 #increment
    if age < 3:
        continue
    else:
        total += ticket
print(f"\nTotal amount to be paid: {total}")
print()