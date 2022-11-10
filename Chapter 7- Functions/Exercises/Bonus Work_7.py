# Bonus Work #7: Multiplication Table - 3/11/22
# Take a number from user. Print its multiplication table upto 10th.

def table(a):
  for i in range(11):
    if (a <= 10):
      result = a * i
      print(f"{a} x {i} = {result}")
print()

table(3)
print()