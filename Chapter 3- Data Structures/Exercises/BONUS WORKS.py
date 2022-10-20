# CHAPTER 3: BONUS WORKS

# ----- LISTS - 29/9/22 -----

    # Creation of List
family_names = ["Jasmin","Fred","Prince","Princess","Alfie","Herbert","Milain","Nikka","Dionisio","Nemia"]

    # Printing the whole list
print("\n-----Printing the Whole List-----")
print(family_names)

    # Printing a specific value through Index
print("\n-----Printing a Specific Value through Index-----")
print(family_names[4])

    # Printing the values from 0-5
print("\n-----Printing the Values from 0-5-----")
print(family_names[0:5])

    # Printing the value from the back
print("\n-----Printing the Value from the Back-----")
print(family_names[-1])

    # Printing the first and last value
print("\n-----Printing the First and Last Value-----")
print(family_names[0])
print(family_names[-1])
print()
#or
print(family_names[0], family_names[9]) 

    # Skipping the first two values and printing the last
print("\n-----Skipping the First Two Values and Printing the Last-----")
print(family_names[2:])

    # Only printing the first four values
print("\n-----Only Printing the First Four Values-----")
print(family_names[:4])

    # Updating Existing Values in a List
print("\n-----Updating Existing Values in a List-----")
family_names[9] = "Linda"
print(family_names)

    # Changing two values in a list
print("\n-----Changing Two Values in a List-----")
family_names[0:1] = "Johnrey","RB"
print(family_names)

    # Inserting New Values inside a List
print("\n----Inserting New Values Inside a List-----")
family_names.insert(1, "Bobby")
print(family_names)

    # Append Function - to add at the end of the list
print("\n----Append Function-----")
family_names.append("abc")
print(family_names)

    # Remove Function
print("\n----Remove Function-----")
family_names.remove("abc")
print(family_names)

    # Pop Function -- remove by index value
print("\n----Pop Function-----")
family_names.pop(8)
print(family_names)

    # Reverse Function
print("\n----Reverse Function-----")
family_names.reverse()
print(family_names)

    # Concatenating Lists
print("\n----Concatening Lists-----")
age = ["35", "40", "16", "8"]
print(family_names + age)

    # Sort Function
print("\n----Sort Function-----")
print(age)
age.sort()
print(age)
print()

# ----- LISTS WITH GRAPHS (LIBRARY) - 29/9/22 -----
# The program can only work in Google Colab

    # To import a library
# import matplotlib.pyplot as plt

    # Printing a Line Graph
# x = [1,2,3,4,5,1]
# y = [1,6,1,6,1,1]
# plt.plot(x,y)

    # Printing a Bar Graph
# plt.barh(x,y, color= ('b','g','r','y'))
# plt.title("This is a Bar Chart")
# plt.xlabel("X values")
# plt.ylabel("Y values")

    # Printing a Pie Chart
# plt.title("This is a Pie Chart")
# plt.pie(x, labels=['no.1','no.2','no.3','no.4','no.5','no.6'])