# CHAPTER 2: BONUS WORKS

# ----- VARIABLES & COMMENTS - 25/9/22 -----

name = "Princess Panilagao"
age = 16
contact_number = "0509103047"
email = "pjspanilagao@hotmail.com"
department = "Creative Computing"
level = "Year 1"

    # Vertical Print
print("\n-----Vertical Print of Variables-----")
print(name)
print(age)
print(contact_number)
print(email)
print(department)
print(level)

    # One-Line Print
print("\n-----One-Line Print of Variables-----")
print(name, age, contact_number, email, department, level)

# ----- FINDING THE AVERAGE & PERCENTAGE MARK OF STUDENT'S SCORES - 25/9/22 -----

    # Activity Instructions:
# 1. Create 5 subjects variables and take marks from the user.
# 2. Calculate the total marks of the students and store those marks in a variable "marks_obtained"
# 3. total_marks is equal to 500.
# 4. Calculate average of the marks and store it in variable "average"
# 5. Calculate percentage of the student and store it in variable "percentage"
# 6. Print average and percentage marks of the student

print("\n-----Finding the Average & Percentage Mark-----")
english = int(input("Enter marks for English: "))
math = int(input("Enter marks for Math: "))
science = int(input("Enter marks for Science: "))
socialstudies = int(input("Enter marks for Social Studies: "))
pe = int(input("Enter marks for PE: "))
print()

marks_obtained = english + math + science + socialstudies + pe
total_marks = 500

average = (marks_obtained) / 5 
percentage = ((marks_obtained) / 500) * 100

print("Average mark of the student is", average)
print("Percentage mark of the student is", percentage)
print()

# ----- TURTLE GRAPHICS - 25/9/22 -----

    # CODE SYNTAX FOR TURTLE 
import turtle

turtle.color('blue')
turtle.forward(100)
turtle.right(50)
turtle.color('red')
turtle.forward(45)