# CHAPTER 6: BONUS WORKS

# ----- SOLO LEARN ACT: TICKET SYSTEM (WHILE LOOP) - 12/10/22 -----
    # Write a program that takes the ages of 5 passengers and outputs the total price for their tickets.

    # The price of a single ticket is $100.
    # For children under 3 years of age, the ticket is free.

print("\n-----Ticketing System-----")
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
print(f"\nTotal: {total}")
print()
