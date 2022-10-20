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

# ----- HEXAGON-TURTLE (FOR LOOP) - 20/10/22 -----
    # Hexagon shape using for loop
import turtle
hexagon = turtle.Turtle()
for x in range(6):
    hexagon.forward(90)
    hexagon.left(300)

# ----- STAR-TURTLE (FOR LOOP) - 20/10/22 -----
    # Star shape using for loop
import turtle
star = turtle.Turtle()
for x in range(6):
    star.forward(100)
    star.right(144)

# ----- CIRCLE LOOP (FOR LOOP) - 20/10/22 -----
    # Circle loop using for loop
import turtle
pen = turtle.Turtle()
circles = 36
radius = 120
angle = 100
for x in range(circles):
    pen.circle(radius)
    pen.left(angle)