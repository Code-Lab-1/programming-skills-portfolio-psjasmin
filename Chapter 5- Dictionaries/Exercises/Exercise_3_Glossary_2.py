## Solutions for Chapter 5: Dictionaries

# Exercise 3: Glossary #2
# Clean up the code from Exercise 6-3 (page 99) by replacing your series of print() calls with a loop.

glossary = {
    "comment": "Used to explain and make the code more readable.",
    "float": "A method that returns a floating-point number for a provided number or string.",
    "list": "A data structure in Python that is a mutable, or changeable, ordered sequence of elements.",
    "function": "A group of related statements that performs a specific task. ",
    "for loop": "Used to iterate over a given sequence, such as lists or strings.",
    "while loop": "Used to iterate over a block of code as long as the test expression (condition) is true.",
    "break": "To end a while loop prematurely.",
    "continue": "Stops the current iteration and continues with the next one.",
    "boolean": "Represent one of two values: True or False .",
    "if statement": "Allows for conditional execution of a statement or group of statements.",

}

print("\n\033[1m\033[1;35m═════════════════════════════════════════════════════════════════════════════════════════════════════════\033[0m\n")

# Loop that runs through the dictionary’s keys and values:
for word, definition in glossary.items():
    print(f"\033[1m\033[1;36m{word.title()}: \033[0m{definition}\n")

print("\033[1m\033[1;35m═════════════════════════════════════════════════════════════════════════════════════════════════════════\033[0m\n")