# Bonus Work #2: SOLO LEARN ACTIVITY (SEARCH ENGINE) - 12/10/22

# Write a program that takes a text and a word as input and passes them to a function called search().
# The search() function should return "Word found" if the word is present in the text, 
# or "Word not found", if it's not.

def search(text, word):
    if word in text:
        print("\n> Word found!")
    else:
        print("\n> Word not found!")

print("\n-----Function: Search Engine-----\n")
text = input("Enter text: ")
word = input("Enter word: ")
search(text, word)
print()