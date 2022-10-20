# CHAPTER 5: BONUS WORKS

# ----- DICTIONARIES - 19/10/22 -----

    # Dictionary Syntax
print("\n-----Printing Dictionaries-----")
student = {
    "Name":"Princess", "Age":16, "Class":"Year 1", "Gender":"Female", "Location":"United Arab Emirates",   
}
print(student["Location"])

    # Printing only first value (key)
print("\n-----Printing only Keys-----")
print(student.keys())

    # Printing only second value (value)
print("\n-----Printing only Values-----")
print(student.values())

    # Printing pairs
print("\n-----Printing Pairs-----")
print(student.items())

    # Changing a value of a key
print("\n-----Changing a Value of a Key-----")
student["Age"] = 20
print(student)

    # Adding a new key
print("\n-----Adding a New Key-----")
student.update({"BG":"A+"})
print(student)

    # Removing a specified key
print("\n-----Removing a Specific Key-----")
student.pop("Name")
print(student)

    # Removing last item by default
print("\n-----Removing Last Item By Default-----")
student.popitem()
print(student)

    # Checking length of a dictionary - total number of pairs in a dictionary
print("\n-----Length of the Dictionary-----")
print(len(student))
print()