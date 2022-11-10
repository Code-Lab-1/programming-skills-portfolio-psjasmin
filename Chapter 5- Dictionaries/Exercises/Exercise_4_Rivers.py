## Solutions for Chapter 5: Dictionaries

# Exercise 4: Rivers
# Make a dictionary containing three major rivers and the country each river runs through.

rivers = {
    "Ganges": "India",
    "Indus": "China",
    "Mississippi": "United States",
}

# Loop to print a sentence about each river:
print("\n\033[1;32m+---------------------------------------------------+\033[0m")
for word, definition in rivers.items():
    print(f"The \033[1m\033[1;32m{word.title()} river \033[0mruns through {definition}.")
print("\033[1;32m+---------------------------------------------------+\033[0m\n")

# Loop to print the name of each river included in the dictionary:
print("\033[1;33m+---------------------------+\033[0m\n  \033[1mRivers in the dictionary: \033[0m")
for word in rivers.keys():
    print(f" > {word.title()}")
print("\033[1;33m+---------------------------+\n\033[0m")

# Loop to print the name of each country included in the dictionary:
print("\033[1;36m+------------------------------+\033[0m\n  \033[1mCountries in the dictionary: \033[0m")
for definition in rivers.values():
    print(f" > {definition.title()}")
print("\033[1;36m+------------------------------+\033[0m\n")