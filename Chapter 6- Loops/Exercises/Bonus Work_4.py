# Bonus Work #4: Letters in a Word (FOR LOOP) - 26/10/22
# Using for loop, write a program that will print all letters in the given words

words = ["Apple", "Banana", "Car", "Dolphin"]
for word in words:
    # This loop is fetching word from the list
    print("\nThe Following lines will print each letters of " + word)
    for letter in word:
        # This loop is fetching letter for the word
        print(letter)
print()