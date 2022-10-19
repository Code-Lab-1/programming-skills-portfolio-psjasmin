## Solutions for Chapter 7: Functions

# Exercise 3: T-Shirt
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.

def make_shirt(size, message):
    """Summarizing the size of the shirt and the message printed on it."""

    print(f"""\n\033[1;36;40m   __   __
 /|  `-´  |\\
/_| -Make |_\   
  |   A   |
  | Shirt |
  |_______|   
    \033[0m 
\033[1;34;40m┌──────────────────────┐
│ Details of the shirt │
└──────────────────────┘\033[0m
o \033[1m Size of the shirt:\033[0m {size}
o \033[1m Message:\033[0m {message} 
    """)

# Positional Arguments:
make_shirt("Medium", "Great things never came from comfort zones!✨")
# Keyword Arguments:
make_shirt(message="Beelieve in yourself!🐝 ", size="Small")