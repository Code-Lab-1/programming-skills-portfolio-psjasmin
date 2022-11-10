# Bonus Work #2: Functions of List (Part 2) - 29/9/22
# Part 2 -- Updating Existing Values | Inserting New Values | Append Function | Remove/Pop Function

list_of_names = ["Archer","Atlas","Rhysand","Azriel","Cassian","Feyre","Sam"]

# Updating Existing Values Inside a List
print("\n-----Updating Existing Values in a List-----")
list_of_names[5] = "Julie"
print(list_of_names)

# Inserting New Values inside a List
print("\n----Inserting New Values Inside a List-----")
list_of_names.insert(1, "Peeta")
print(list_of_names)

# Append Function - to add at the end of the list
print("\n----Append Function-----")
list_of_names.append("Elizabeth")
print(list_of_names)

# Remove Function
print("\n----Remove Function-----")
list_of_names.remove("Elizabeth")
print(list_of_names)

# Pop Function -- remove by index value
print("\n----Pop Function-----")
list_of_names.pop(6)
print(list_of_names)
print()