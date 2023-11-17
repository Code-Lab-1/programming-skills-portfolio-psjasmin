# Bonus Work #2: Finding the Average and Percentage Mark of Student's Scores - 25/9/22

    ## ACTIVITY INSTRUCTIONS:
# 1. Create 5 subjects variables and take marks from the user.
# 2. Calculate the total marks of the students and store those marks in a variable "marks_obtained"
# 3. total_marks is equal to 500.
# 4. Calculate average of the marks and store it in variable "average"
# 5. Calculate percentage of the student and store it in variable "percentage"
# 6. Print average and percentage marks of the student

print("\n-----Finding the Average & Percentage Mark-----\n")
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