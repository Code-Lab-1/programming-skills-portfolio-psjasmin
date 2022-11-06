## Solutions for Chapter 5: Dictionaries

# Exercise 5: Pets
# Make several dictionaries, where each dictionary represents a different pet.

# Empty list to store the pets in:
pets = []

# Dictionary including the kind of animal and the owner’s name:
pet = {
    "Name":"Cookie",
    "Owner":"Elizabeth",
    "Animal Type":"guinea pig",
    "Weight": 1.2,
    "Food it eats":"hays",
}
pets.append(pet) #to add at the end of the list

pet = {
    "Name":"Apollo",
    "Owner":"Henry",
    "Animal Type":"dog",
    "Weight": 25,
    "Food it eats":"peanut butter",
}
pets.append(pet)

pet = {
    "Name":"Donatello",
    "Owner":"Ryan",
    "Animal Type":"turtle",
    "Weight": 1.8,
    "Food it eats":"vegetables\n",
}
pets.append(pet)

# To display information about each pet:
print("\n\033[1m\033[1;36m ______   ______     ______   ______    ")
print("/\  == \ /\  ___\   /\__  _\ /\  ___\   ")
print("\ \  _-/ \ \  __\   \/_/\ \/ \ \___  \  ")
print(" \ \_\    \ \_____\    \ \_\  \/\_____\ ")
print("  \/_/     \/_____/     \/_/   \/_____/ \033[0m")

for pet in pets:
    print("\n\033[1;34m+----------------------------------+\033[0m")
    print(f"\033[1m\033[1;36m  Information about {pet['Name'].title()}:\033[0m")
    for key, value in pet.items():
        print(f"     {key}: {value}")