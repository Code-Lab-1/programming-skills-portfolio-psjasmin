## Solutions for Chapter 4: Control Flow

# Exercise 3: Alien Colors #3
# Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.

# Green Version:
alien_color = 'green'

if alien_color == 'green':
    print("\n\033[1;32m+------------------------------+")
    print("| You just earned 5 points! \U0001F47D |") # \U0001F47D -alien emoji
    print("+------------------------------+\033[0m\n")
elif alien_color == 'yellow':
    print("\n\033[1;33m+-------------------------------+")
    print("| You just earned 10 points! \U0001F47D |") 
    print("+-------------------------------+\033[0m\n")
else:
    print("\n\033[1;31m+-------------------------------+")
    print("| You just earned 15 points! \U0001F47D |")
    print("+-------------------------------+\033[0m\n")

# Yellow Version:
alien_color = 'yellow'

if alien_color == 'green':
    print("\n\033[1;32m+------------------------------+")
    print("| You just earned 5 points! \U0001F47D |") # \U0001F47D -alien emoji
    print("+------------------------------+\033[0m\n")
elif alien_color == 'yellow':
    print("\n\033[1;33m+-------------------------------+")
    print("| You just earned 10 points! \U0001F47D |") 
    print("+-------------------------------+\033[0m\n")
else:
    print("\n\033[1;31m+-------------------------------+")
    print("| You just earned 15 points! \U0001F47D |")
    print("+-------------------------------+\033[0m\n")

# Red Version:
alien_color = 'red'

if alien_color == 'green':
    print("\n\033[1;32m+------------------------------+")
    print("| You just earned 5 points! \U0001F47D |") # \U0001F47D -alien emoji
    print("+------------------------------+\033[0m\n")
elif alien_color == 'yellow':
    print("\n\033[1;33m+-------------------------------+")
    print("| You just earned 10 points! \U0001F47D |") 
    print("+-------------------------------+\033[0m\n")
else:
    print("\n\033[1;31m+-------------------------------+")
    print("| You just earned 15 points! \U0001F47D |")
    print("+-------------------------------+\033[0m\n")