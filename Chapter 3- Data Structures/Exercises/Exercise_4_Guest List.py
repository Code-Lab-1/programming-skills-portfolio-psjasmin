## Solutions for Chapter 3: Data Structures

# Exercise 4: Guest List
# Make a list that includes at least three people you’d like to invite to dinner. 
# Then use your list to print a message to each person, inviting them to dinner.

guests = ["Jane Austen", "Suzanne Collins", "Stephen King"]

print("\n\033[1;35;40m.-=-=-=-=-=-=-=-=-=-=-=-.")
print("|                       |")
print("!   ⋆｡˚  WE ARE         !")
print(":       INVITING        :")
print(".       YOU TO A        .")
print("!     DINNER PARTY ⋆｡˚  !")
print("|                       |")
print(".-=-=-=-=-=-=-=-=-=-=-=-. \033[0m")

# \033[1m - makes text bold
name = guests[0].title()
print(f"\n\033[1m\033[1;36;40mDear {name},\033[0m\n""Gourmet delights and an evening of culinary adventure await you at the home of Mr. Moriarty at 33 Petunia Way, Birmingham.\n˗ˏˋ Please join us for drinks, followed by dinner on the 20th of November at 7:00 pm.´ˎ˗\n")

name = guests[1].title()
print(f"\033[1m\033[1;36;40mDear {name},\033[0m\n""Gourmet delights and an evening of culinary adventure await you at the home of Mr. Moriarty at 33 Petunia Way, Birmingham.\n˗ˏˋ Please join us for drinks, followed by dinner on the 20th of November at 7:00 pm.´ˎ˗\n")

name = guests[2].title()
print(f"\033[1m\033[1;36;40mDear {name},\033[0m\n""Gourmet delights and an evening of culinary adventure await you at the home of Mr. Moriarty at 33 Petunia Way, Birmingham.\n˗ˏˋ Please join us for drinks, followed by dinner on the 20th of November at 7:00 pm.´ˎ˗\n")