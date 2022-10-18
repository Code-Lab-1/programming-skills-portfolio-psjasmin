## Solutions for Chapter 6: Loops

# Exercise 2: Movie Tickets
# A movie theater charges different ticket prices depending on a person’s age.

print("\n\033[1;33;40m....................................")
print("\033[1;33;40m: WELCOME TO THE MOVIE THEATRE !🍿 :")
print("\033[1;33;40m:..................................:\033[0m\n")

print("\033[1;30;40m(Enter 'quit' when you are finished)\033[0m\n")

while True:
    age = int(input("\033[1mEnter age: \033[0m"))
    if age == 'quit':
        break
    if age < 3:
        print("  \033[1m\033[1;32;40mThe cost of your movie ticket is free!\033[0m\n")
    elif age <12:
        print("  \033[1m\033[1;32;40mThe cost of your movie ticket is $10!\033[0m\n")
    else:
        print("  \033[1m\033[1;32;40mThe cost of your movie ticket is $15!\033[0m\n")