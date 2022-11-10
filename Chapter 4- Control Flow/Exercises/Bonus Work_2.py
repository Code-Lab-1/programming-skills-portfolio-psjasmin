# Bonus Work #2: Triangle Checker - 5/10/22

    ## ACTIVITY INSTRUCTIONS
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
    print("> This is an equilateral triangle.\n")
  elif (side1 == side2 or side1 == side3 or side2 == side3):
    print("> This is an iscosceles triangle.\n")
  else:
    print("> This is a scalene triangle.\n")
else:
  print("This is not a triangle!\n")