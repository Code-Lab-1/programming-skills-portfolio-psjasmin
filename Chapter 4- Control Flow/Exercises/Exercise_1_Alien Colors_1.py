## Solutions for Chapter 4: Control Flow

# Exercise 1: Alien Colors #1
# •Imagine an alien was just shot down in a game. Write an if statement to test whether the alien’s color is green.
# •Write one version of this program that passes the if test and another that fails.

# Passed version:
alien_color = 'green'

if alien_color == 'green':
    print("\n\033[1;32m+------------------------------+")
    print("| You just earned five points! |")
    print("+------------------------------+\033[0m\n")

# Failed version:
alien_color = 'red'

if alien_color == 'green':
    print("\n\033[1;32m+------------------------------+")
    print("| You just earned five points! |")
    print("+------------------------------+\033[0m\n")