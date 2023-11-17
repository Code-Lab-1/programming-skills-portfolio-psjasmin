# Bonus Work #3: Dictionaries (Part 3) - 19/10/22
# Part 3 -- Pop Function | Len Function

student = {
    "Name":"Princess", "Age":16, "Class":"Year 1", "Gender":"Female", "Location":"United Arab Emirates",   
}

# Removing a specified key
print("\n-----Removing a Specific Key-----")
student.pop("Name")
print(student)

# Removing last item by default
print("\n-----Removing Last Item By Default-----")
student.popitem()
print(student)

# Checking length of a dictionary - (total number of pairs in a dictionary)
print("\n-----Length of the Dictionary-----")
print(len(student))
print()