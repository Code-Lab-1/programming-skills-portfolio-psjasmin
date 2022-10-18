## Solutions for Chapter 4: Control Flow

# Exercise 4: Stages of Life
# Write an if-elif-else chain that determines a person’s stage of life.

print("\n\033[1m------- What stage of life are you in? -------\033[0m")
age = 13

if age < 2:
    print("\n┌─────────────────┐\n│ You are a baby! │\n└─────────────────┘\n")
elif age < 4:
    print("\n┌────────────────────┐\n│ You are a toddler! │\n└────────────────────┘\n")
elif age < 13:
    print("\n┌────────────────┐\n│ You are a kid! │\n└────────────────┘\n")
elif age < 20: 
    print("\n┌─────────────────────┐\n│ You are a teenager! │\n└─────────────────────┘\n")
elif age < 65:
    print("\n┌───────────────────┐\n│ You are an adult! │\n└───────────────────┘\n")
else:
    print("\n┌───────────────────┐\n│ You are an elder! │\n└───────────────────┘\n")