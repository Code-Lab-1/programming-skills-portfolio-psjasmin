# CHAPTER 6: BONUS WORKS

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