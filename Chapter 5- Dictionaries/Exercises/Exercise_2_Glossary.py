## Solutions for Chapter 5: Dictionaries

# Exercise 2: Glossary
# A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.

glossary = {
    "comment": "Used to explain and make the code more readable.",
    "list": "A data structure in Python that is a mutable, or changeable, ordered sequence of elements.",
    "function": "A group of related statements that performs a specific task. ",
    "for_loop": "Used to iterate over a given sequence, such as lists or strings.",
    "while_loop": "Used to iterate over a block of code as long as the test expression (condition) is true.",
}

print("\n╔═══════════════════════════════════════════════════════════════════════════════════════════════════════╗")

name = "║ \033[1mComment : \033[0m"
print(name + glossary["comment"] + "                                            ║")
print('║                                                                                                       ║')

name = "║ \033[1mList : \033[0m"
print(name + glossary["list"] + "     ║")
print('║                                                                                                       ║')

name = "║ \033[1mFunction : \033[0m"
print(name + glossary["function"] + "                              ║")
print('║                                                                                                       ║')

name = "║ \033[1mFor Loop : \033[0m"
print(name + glossary["for_loop"] + "                           ║")
print('║                                                                                                       ║')

name = "║ \033[1mWhile Loop : \033[0m"
print(name + glossary["while_loop"] + " ║")

print("╚═══════════════════════════════════════════════════════════════════════════════════════════════════════╝\n")