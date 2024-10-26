# Student inputs their grade
grade = int(input("Hello,input your grade: "))

# Grade is checked and displayed to the student
if grade >= 90 and grade <= 100:
    print(f"Your grade of {grade} is an A")
elif grade >= 80 and grade <= 90:
    print(f"Your grade of {grade} is a B")
elif grade >= 70 and grade <= 80:
    print(f"Your grade of {grade} is a C")
elif grade >= 60 and grade <= 70:
    print(f"Your grade of {grade} is a D")
elif grade < 60:
    print(f"Your grade of {grade} is an F")
else:
    print("Invalid Entry")

