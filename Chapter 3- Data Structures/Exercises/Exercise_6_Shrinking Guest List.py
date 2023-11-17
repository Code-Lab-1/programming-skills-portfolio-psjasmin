## Solutions for Chapter 3: Data Structures

# Exercise 6: Shrinking Guest List
# You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.

guests = ["Jane Austen", "Suzanne Collins", "Stephen King"]

print("\n\033[1;35m.-=-=-=-=-=-=-=-=-=-=-=-.")
print("|                       |")
print("!   ⋆｡˚  WE ARE         !")
print(":       INVITING        :")
print(".       YOU TO A        .")
print("!     DINNER PARTY ⋆｡˚  !")
print("|                       |")
print(".-=-=-=-=-=-=-=-=-=-=-=-. \033[0m")

# \033[1m - makes text bold
name = guests[0].title()
print(f"\n\033[1m\033[1;36mDear {name},\033[0m\n""Gourmet delights and an evening of culinary adventure await you at the home of Mr. Moriarty at 33 Petunia Way, Birmingham.\n˗ˏˋ Please join us for drinks, followed by dinner on the 20th of November at 7:00 pm.´ˎ˗\n")

name = guests[1].title()
print(f"\033[1m\033[1;36mDear {name},\033[0m\n""Gourmet delights and an evening of culinary adventure await you at the home of Mr. Moriarty at 33 Petunia Way, Birmingham.\n˗ˏˋ Please join us for drinks, followed by dinner on the 20th of November at 7:00 pm.´ˎ˗\n")

name = guests[2].title()
print(f"\033[1m\033[1;36mDear {name},\033[0m\n""Gourmet delights and an evening of culinary adventure await you at the home of Mr. Moriarty at 33 Petunia Way, Birmingham.\n˗ˏˋ Please join us for drinks, followed by dinner on the 20th of November at 7:00 pm.´ˎ˗\n")

print("\033[1;31m" + (guests[1]) + " can't make it to the dinner.\033[0m")

guests[1] = "William Shakespeare" # Updating the list

# Updated Guest Invitations
print("\n\033[1;35m.-=-=-=-=-=-=-=-=-=-=-=-.")
print("|                       |")
print("!   ⋆｡˚  WE ARE         !")
print(":       INVITING        :")
print(".       YOU TO A        .")
print("!     DINNER PARTY ⋆｡˚  !")
print("|                       |")
print(".-=-=-=-=-=-=-=-=-=-=-=-. \033[0m")

name = guests[0].title()
print(f"\n\033[1m\033[1;36mDear {name},\033[0m\n""Gourmet delights and an evening of culinary adventure await you at the home of Mr. Moriarty at 33 Petunia Way, Birmingham.\n˗ˏˋ Please join us for drinks, followed by dinner on the 20th of November at 7:00 pm.´ˎ˗\n")

name = guests[1].title()
print(f"\033[1m\033[1;36mDear {name},\033[0m\n""Gourmet delights and an evening of culinary adventure await you at the home of Mr. Moriarty at 33 Petunia Way, Birmingham.\n˗ˏˋ Please join us for drinks, followed by dinner on the 20th of November at 7:00 pm.´ˎ˗\n")

name = guests[2].title()
print(f"\033[1m\033[1;36mDear {name},\033[0m\n""Gourmet delights and an evening of culinary adventure await you at the home of Mr. Moriarty at 33 Petunia Way, Birmingham.\n˗ˏˋ Please join us for drinks, followed by dinner on the 20th of November at 7:00 pm.´ˎ˗\n")

# Shrinking Guest List
print("\033[1;31mMy deepest apologies! I can only invite two guests to the dinner!\033[0m\n")

print((guests[2]) + ", I sincerely apologize I won't be able to invite you to dinner.")
guests.pop(2)

print("\n\033[1;35m.-=-=-=-=-=-=-=-=-=-=-=-.")
print("|                       |")
print("!   ⋆｡˚  WE ARE         !")
print(":       INVITING        :")
print(".       YOU TO A        .")
print("!     DINNER PARTY ⋆｡˚  !")
print("|                       |")
print(".-=-=-=-=-=-=-=-=-=-=-=-. \033[0m")

name = guests[0].title()
print(f"\n\033[1m\033[1;36mDear {name},\033[0m\n""You are still invited to gourmet delights and an evening of culinary adventure!\n˗ˏˋ Please join us for drinks, followed by dinner on the 20th of November at 7:00 pm.´ˎ˗\n")

name = guests[1].title()
print(f"\033[1m\033[1;36mDear {name},\033[0m\n""You are still invited to gourmet delights and an evening of culinary adventure!\n˗ˏˋ Please join us for drinks, followed by dinner on the 20th of November at 7:00 pm.´ˎ˗\n")

del guests[0] # emptying out the list
del guests[0]
print(guests)