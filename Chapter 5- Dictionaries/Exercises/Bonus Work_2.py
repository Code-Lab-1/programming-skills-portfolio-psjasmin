# Bonus Work #2: Dictionaries (Part 2) - 19/10/22
# Part 2 -- Printing Pairs | Changing the value of a Key | Adding a new Key

student = {
    "Name":"Princess", "Age":16, "Class":"Year 1", "Gender":"Female", "Location":"United Arab Emirates",   
}

# Printing Pairs
print("\n-----Printing Pairs-----")
print(student.items())

# Changing the Value of a Key
print("\n-----Changing a Value of a Key-----")
student["Age"] = 20
print(student)

# Adding a New Key
print("\n-----Adding a New Key-----")
student.update({"BG":"A+"})
print(student)
print()