# Bonus Work #3: SOLO LEARN ACTIVITY (RETURN) - 12/10/22

# Calculate the area of a given rectangle.
# Write a program that takes the width & length as input and output the area of the rectangle.
# Call the function for the given outputs.

def area(x, y):
    return x*y

print("\n-----Function: Calculating Area-----\n")
w = int(input("Enter width: "))
h = int(input("Enter height: "))

print(f"\nThe are of the rectangle is {area(w,h)}\n") #call the function