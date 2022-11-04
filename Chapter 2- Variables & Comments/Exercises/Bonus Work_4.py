# Bonus Work #4: Getting Details From A User - 4/11/22
# Take a user's name, age, and the country they live in using various variables.

name = input("\n> What is your name? ")
print(f"Hi {name}! Nice to meet you ^-^")

age = int(input("\n> How old are you? "))
if age <= 20:
    print(f"Wow, you're {age}? You're very young!\n")
else:
    print(f"Wow, you're {age}? You're very old!\n")

place = input("> Where do you live? ")
print(f"You live in such a wonderful place <3\n")