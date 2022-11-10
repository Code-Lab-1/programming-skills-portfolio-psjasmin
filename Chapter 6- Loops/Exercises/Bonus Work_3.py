# Bonus Work #3: Infinite Circle (FOR LOOP) - 20/10/22
# Make a circle loop using for loop

import turtle
pen = turtle.Turtle()
circles = 36
radius = 120
angle = 100
for x in range(circles):
    pen.circle(radius)
    pen.left(angle)