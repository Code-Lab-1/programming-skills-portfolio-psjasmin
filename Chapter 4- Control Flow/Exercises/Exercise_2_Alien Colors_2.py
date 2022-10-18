## Solutions for Chapter 4: Control Flow

# Exercise 2: Alien Colors #2
# Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.

# Running the if block:
alien_color = 'green'

if alien_color == 'green':
    print("\n\033[1;32;40m+---------------------------------+")
    print("| You just earned five points! \U0001F47D |") # \U0001F47D -alien emoji
    print("+---------------------------------+\033[0m\n")
else:
    print("\033[1;34;40m+---------------------------------+")
    print("| You just earned ten points! \U0001F47D |")
    print("+---------------------------------+\033[0m\n")

# Running the else block:
alien_color = 'yellow'

if alien_color == 'green':
    print("\n\033[1;32;40m+---------------------------------+")
    print("| You just earned five points! \U0001F47D |")
    print("+---------------------------------+\033[0m\n")
else:
    print("\033[1;34;40m+--------------------------------+")
    print("| You just earned ten points! \U0001F47D |")
    print("+--------------------------------+\033[0m\n")