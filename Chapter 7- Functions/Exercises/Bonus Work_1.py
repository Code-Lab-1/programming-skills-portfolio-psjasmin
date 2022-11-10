# Bonus Work #1: SOLO LEARN ACTIVITY (ARGUMENTS) - 12/10/22

# Write a program that defines a function printBill(), which takes one string argument and outputs formatted text.
# Takes a user input and calls the function by passing the input as its argument.

def printBill(text):
    print("=======")
    print(text)
    print("=======\n")

print("\n-----Function: Arguments-----\n")
user = input("Enter text: ")
printBill(user)
print()