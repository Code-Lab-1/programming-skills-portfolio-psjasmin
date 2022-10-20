# CHAPTER 7: BONUS WORKS

# ----- SOLO LEARN ACT #1: ARGUMENTS - 12/10/22 -----
    # Write a program that defines a function printBill(), which takes one string argument and outputs formatted text.
    # Takes a user input and calls the function by passing the input as its argument.

def printBill(text):
    print("=======")
    print(text)
    print("=======\n")

print("\n-----Function: Arguments-----")
user = input("Enter text: ")
printBill(user)

# ----- SOLO LEARN ACT #2: SEARCH ENGINE - 12/10/22 ----- 
    # Write a program that takes a text and a word as input and passes them to a function called search().
    # The search() function should return "Word found" if the word is present in the text, 
    # or "Word not found", if it's not.

def search(text, word):
    if word in text:
        print("\nWord found!")
    else:
        print("\nWord not found!")

print("\n-----Function: Search Engine-----")
text = input("Enter text: ")
word = input("Enter word: ")
search(text, word)

# ----- SOLO LEARN ACT #3: RETURN - 12/10/22 -----
    # Calculate the area of a given rectangle.
    # Write a program that takes the width & length as input and output the area of the rectangle.
    # Call the function for the given outputs.

def area(x, y):
    return x*y

print("\n-----Function: Calculating Area-----")
w = int(input("Enter width: "))
h = int(input("Enter height: "))

print(f"\nArea: {area(w,h)}\n") #call the function