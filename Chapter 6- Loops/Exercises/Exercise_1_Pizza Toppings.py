## Solutions for Chapter 6: Loops

# Exercise 1: Pizza Toppings
# Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value.

print("\n\033[1;31m     ,------. ,--.                       ")
print("     |  .--. '`--',-----.,-----. ,--,--.")
print("     |  '--' |,--.`-.  / `-.  / ' ,-.  | ")
print("     |  | --' |  | /  `-. /  `-.\ '-'  | ")
print("     `--'     `--'`-----'`-----' `--`--' \033[0m")

print("+--------------------------------------------+\n\033[1m| What topping would you like on your pizza? |\033[0m\n+--------------------------------------------+")
print("\033[1;30m     (Enter 'quit' when you are finished)\033[0m\n")

prompt = ("\033[1m\033[1;31mEnter topping: \033[0m")

while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f"  I'll add {topping} to your pizza!\n")
    else:
        break
print()