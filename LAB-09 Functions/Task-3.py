def grade_gpa(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"


marks = int(input("Enter your marks: "))
print("Your grade is", grade_gpa(marks))
