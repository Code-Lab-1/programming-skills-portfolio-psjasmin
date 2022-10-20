# CHAPTER 7: BONUS WORKS
# ----- PANDA ACTIVITY: TURTLE PYTHON - 20/10/22 -----
    # Drawing Panda Using Turtle Graphics

import turtle
pen = turtle.Turtle()

def ring(col, rad):
    # Set the fill
    pen.fillcolor(col)
    #Start filling the color
    pen.begin_fill()
    # Draw a circle
    pen.circle(rad)
    # Ending the filling of the color
    pen.end_fill()

        #### Drawing the Ears ####
## First Ear (base color)
pen.up()
pen.setpos(-35, 95)
pen.down
ring('light sky blue', 30)

## Second Ear (base color)
pen.up()
pen.setpos(50, 95)
pen.down
ring('light sky blue', 30)

## First Ear (inner color)
pen.up()
pen.setpos(-35, 97)
pen.down
ring('light cyan', 25)

## Second Ear (inner color)
pen.up()
pen.setpos(50, 97)
pen.down
ring('light cyan', 25)


        #### Drawing the Face ####
pen.up()
pen.setpos(5, 15)
pen.down()
ring('alice blue', 60)

        #### Drawing the Eyes ####
# First Eye (base color)
pen.up()
pen.setpos(-20, 75)
pen.down()
ring('steel blue', 15)

# Second Eye (base color)
pen.up()
pen.setpos(30, 75)
pen.down()
ring('steel blue', 15)

# First Eye (inner color)
pen.up()
pen.setpos(-20, 77)
pen.down()
ring('white smoke', 10)

# Second Eye (inner color)
pen.up()
pen.setpos(30, 77)
pen.down()
ring('white smoke', 10)

        #### Drawing the Nose ####
pen.up()
pen.setpos(5, 55)
pen.down
ring('light sky blue', 8)
 
        #### Drawing the Mouth ####
pen.up()
pen.setpos(5, 55)
pen.down()
pen.right(90)
pen.circle(5, 180)
pen.up()
pen.setpos(5, 55)
pen.down()
pen.left(360)
pen.circle(5, -180)
pen.hideturtle()