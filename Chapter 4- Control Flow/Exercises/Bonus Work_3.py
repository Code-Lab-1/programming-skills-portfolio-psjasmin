# Bonus Work #3: SOLO LEARN ACTIVITY (AGE GROUP) - 10/10/22
# Write a program that takes a user's age and outputs their corresponding age group.

    ## ACTIVITY INSTRUCTIONS
# Child = less than or equal to 11
# Teen = more or equal to 12 and less or equal to 17
# Adult = more or equal to 18 and less or equal to 64

print("\n-----Input age to know your corresponding age group-----")
age = int(input("\nEnter age: "))
if (age <= 11):
    print("You are a Child!")
elif (age >=12 and age <=17):
    print("You are a Teen!")
elif (age >=18 and age <=64):
    print("You are an Adult!")
else:
    print("Not in the age group!")
print()