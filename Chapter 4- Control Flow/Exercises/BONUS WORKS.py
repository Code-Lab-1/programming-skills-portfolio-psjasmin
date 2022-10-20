# CHAPTER 4: BONUS WORKS

# ----- CONDITIONAL STATEMENTS - 13/10/22 -----

    # If Statements
print("\n-----If Statements-----")
marks = int(input("\nEnter marks: "))
if (marks >40):
  print("You have passed the subject.")

    # If else Statements
    # Write a program to check whether the user is allowed to drive or not.
print("\n-----If Else Statements-----")
age = int(input("\nEnter age: "))
if (age >= 18):
  print("You are allowed to drive.")
else:
  print("You are not allowed to drive.")

    # If-elif-else Statements
    # Write a program to check whether a number is positive, negative, or zero.
print("\n-----If-Elif-Else Statements-----")
num = int(input("\nEnter number: "))

if (num <0):
  print("negative")
elif (num >0):
  print("positive")
else:
    print("zero")

# ----- TRIANGLE CHECKER - 5/10/22 -----

    # Write a program to check if three numbers are a triangle.
    # Determine what type of triangle did the user input.

print("\n-----To check if three numbers are a triangle and its triangle type-----")
side1 = int(input("\nEnter value of first side: "))
side2 = int(input("Enter value of second side: "))
side3 = int(input("Enter value of third side: "))

result = float(side1 + side2 + side3)
print()
if (result ==180):
  print ("This is a triangle!")
  if (side1 ==side2 ==side3): # nested if-elif-else statement
    print("This is an equilateral triangle.")
  elif (side1 == side2 or side1 == side3 or side2 == side3):
    print("This is an iscosceles triangle.")
  else:
    print("This is a scalene triangle.")

else:
  print("This is not a triangle!")

# ----- SOLO LEARN ACT #1: AGE GROUP - 10/10/22 -----
    # Write a program that takes a user's age and outputs their corresponding age group.

print("\n-----Input age to know your corresponding age group-----")
age = int(input("\nEnter age: "))
if (age <= 11):
    print("Child")
elif (age >=12 and age <=17):
    print("Teen")
elif (age >=18 and age <=64):
    print("Adult")
else:
    print("Not in the age group")

# ----- SOLO LEARN ACT #2: BMI CALCULATOR - 12/10/22 -----
    # Write a program that takes a user's height and weight and outputs their corresponding BMI category.

print("\n-----BMI Calculator-----")
weight = int(input("\nEnter weight: "))
height = float(input("Enter height: "))
print()

BMI = float
BMI = weight / height**2

if BMI < 18.5:
    print("Underweight\n")
elif BMI >= 18.5 and BMI <25:
    print("Normal\n")
elif BMI >= 25 and BMI <30:
    print("Overweight\n")
else:
    print("Obesity\n")