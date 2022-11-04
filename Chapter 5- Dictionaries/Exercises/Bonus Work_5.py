# Bonus Work #5: Calculate the sum - 4/11/22
# Write a program to find the sum of all items in a Dictionary.

def returnSum(calculate): # Function to print the sum
    return sum(calculate.values())

calculate = {'num1': 18, 'num2': 50, 'num3': 3} # Dictionary with the values
print("\nSum of all items in the dictionary: ", returnSum(calculate))
print()