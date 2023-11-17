# Bonus Work #6: Finding the Average & Percentage - 3/11/22
# Take 4 numbers from a user. Calculate the average and percentage of the 4 numbers and print.

def calculate(a,b,c,d):
  total = a+b+c+d
  average = (total) / 4
  percentage = (total/400)*100

  print(f"\nThe average is {average}")
  print(f"The percentage is {percentage}\n")

calculate(10,20,30,40)