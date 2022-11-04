# Bonus Work #1: Conditional Statements - 13/10/22

# If Statements
# Write a program to check if a student passed a subject (grade should be above 40).

print("\n-----If Statements-----")
marks = int(input("\nEnter marks: "))
if (marks >40):
  print("You have passed the subject!")

# If else Statements
# Write a program to check whether the user is allowed to drive or not.

print("\n-----If Else Statements-----")
age = int(input("\nEnter age: "))
if (age >= 18):
  print("You are allowed to drive!")
else:
  print("You are NOT allowed to drive!")

# If-elif-else Statements
# Write a program to check whether a number is positive, negative, or zero.

print("\n-----If-Elif-Else Statements-----")
num = int(input("\nEnter number: "))

if (num <0):
  print("Negative!")
elif (num >0):
  print("Positive!")
else:
    print("Zero!")
print()