## Solutions for Chapter 6: Loops

# Exercise 3: Infinity
# Write a loop that never ends, and run it. 
# To end the loop, press ctrl-C or close the window displaying the output.

print("\n\033[1;35m+-----------------------+\033[0m")
age = int(input("\033[1mEnter a number: \033[0m"))
while True:
    if age == 'quit':
        break
    if age < 3:
        print("  \033[1;35mInvalid Value! :)\033[0m\n")
    else:
        print("  \033[1;35mInvalid Value! :)\033[0m\n")