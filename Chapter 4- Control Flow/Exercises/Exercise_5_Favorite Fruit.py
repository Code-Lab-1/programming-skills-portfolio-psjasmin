## Solutions for Chapter 4: Control Flow

# Exercise 5: Favorite Fruit
# Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.

favorite_fruits = ["mango", "melon", "strawberry"]

if "mango" in favorite_fruits:
    print("""\n...............................
: You really like mangoes! \U0001F96D :
:.............................:\n""")

if "melon" in favorite_fruits:
    print("""..............................
: You really like melons! \U0001F348 :
:............................:\n""")

if "cherry" in favorite_fruits:
    print("""................................
: You really like cherries! \U000FE04F :
:..............................:\n""")

if "watermelon" in favorite_fruits:
    print("""...................................
: You really like watermelons! \U000FE054 :
:.................................:\n""")

if "strawberry" in favorite_fruits:
    print("""....................................
: You really like strawberries! \U0001F353 :
:..................................:\n""")