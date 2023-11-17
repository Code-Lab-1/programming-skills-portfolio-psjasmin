# Bonus Work #9: Checking if a number is prime or not - 10/11/22
# Write a program that takes a number from user and check whether the number is prime or not.

def prime(num):
  if num > 1:
      for i in range(2, int(num/2)+1):
        # If a number is divisible by any number between
        # 2 and n / 2, it is not prime
          if (num % i) == 0:
              print(f"\n{num} is not a prime number!\n")
              break
      else:
        print(f"\n{num} is a prime number!\n")
  else:
      print(f"\n{num} is not a prime number!\n")
prime(7)