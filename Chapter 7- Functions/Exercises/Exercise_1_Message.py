## Solutions for Chapter 7: Functions

# Exercise 1: Message
# Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter.

def display_message():
    """Displays a message about what I'm learning this chapter."""
    print("\n\033[1m                   What I'm learning about in this chapter:\033[0m")
    print("""+----------------------------------------------------------------------------+
| This chapter we are learning about functions.                              |
| A function is a group of related statements that performs a specific task. |
| Functions help break programs into smaller and modular chunks.             |
+----------------------------------------------------------------------------+\n""")

display_message()