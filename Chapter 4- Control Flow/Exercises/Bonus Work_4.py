# Bonus Work #4: SOLO LEARN ACTIVITY (BMI CALCULATOR) - 12/10/22
# Write a program that takes a user's height and weight and outputs their corresponding BMI category.

    ## ACTIVITY INSTRUCTIONS
# BMI is calculated using this formula: weight/height^2
# Underweight = less than 18.5
# Normal = more or equal to 18.5 and less than 25
# Overweight = more or equal to 25 and less than 30
# Obesity = 30 or more

print("\n-----BMI Calculator-----")
weight = int(input("\nEnter weight: "))
height = float(input("Enter height: "))
print()

BMI = float
BMI = weight / height**2

if BMI < 18.5:
    print("> Underweight!\n")
elif BMI >= 18.5 and BMI <25:
    print("> Normal!\n")
elif BMI >= 25 and BMI <30:
    print("> Overweight!\n")
else:
    print("> Obesity!\n")