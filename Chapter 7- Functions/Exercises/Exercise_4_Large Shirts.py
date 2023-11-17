## Solutions for Chapter 7: Functions

# Exercise 4: Large Shirts
# Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.

def make_shirt(size = "Large", message = "I love Python!"):
    """Summarizing the size of the shirt and the message printed on it."""

    print(f"""\n\033[1;36m   __   __
 /|  `-´  |\\
/_| -Make |_\   
  |   A   |
  | Shirt |
  |_______|   
    \033[0m 
\033[1;34m┌──────────────────────┐
│ Details of the shirt │
└──────────────────────┘\033[0m
o \033[1m Size of the shirt:\033[0m {size}
o \033[1m Message:\033[0m {message} 
    """)

# Large shirt w/ default message:
make_shirt()
# Medium shirt w/ default message:
make_shirt(size="Medium")
# Shirt of any size with a different message:
make_shirt(message="Beelieve in yourself!🐝 ", size="Small")