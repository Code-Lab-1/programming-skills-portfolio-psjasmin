# CHAPTER 6: BONUS WORKS

# ----- CLASS ACTIVITY (FOR LOOPS) - 26/10/22 -----

    # First Solution: One Loop to print each letter of a word
print("\n-----FIRST SOLUTION-----\n")
words = ["Apple", "Banana", "Car", "Dolphin"]
for word in words:
    # This loop is fetching word from the list
    print("The Following lines will print each letters of " + word)
    for letter in word:
        # This loop is fetching letter for the word
        print(letter)
    print()

    # Second Solution: Different Loops to print each letter of a word
print("\n-----SECOND SOLUTION-----\n")
# The following lines will print each letters of Apple
print("The following lines will print each letters of Apple")
apple = "Apple"
for letter in apple:
  print(letter)
print()

# The following lines will print each letters of Banana
print("The following lines will print each letters of Banana")
banana = "Banana"
for letter in banana:
  print(letter)
print()

# The following lines will print each letters of Car
print("The following lines will print each letters of Car")
car = "Car"
for letter in car:
  print(letter)
print()

# The following lines will print each letters of Dolphin
print("The following lines will print each letters of Dolphin")
dolphin = "Dolphin"
for letter in dolphin:
  print(letter)
print()