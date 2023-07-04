total_marks_FCP = int(input("Enter total marks in FCP: "))
total_marks_Math = int(input("Enter total marks in Math: "))
total_marks_EE = int(input("Enter total marks in EE: "))

obtained_marks_FCP = int(input("Enter obtained marks in FCP: "))
obtained_marks_Math = int(input("Enter obtained marks in Math: "))
obtained_marks_EE = int(input("Enter obtained marks in EE: "))

percentage_FCP = obtained_marks_FCP / total_marks_FCP * 100
percentage_Math = obtained_marks_Math / total_marks_Math * 100
percentage_EE = obtained_marks_EE / total_marks_EE * 100

total_marks = total_marks_EE + total_marks_FCP + total_marks_Math
obtained_marks = obtained_marks_Math + obtained_marks_FCP + obtained_marks_EE

all_subject_percentage = obtained_marks / total_marks * 100

print()
print("Percentage in FCC", percentage_FCP)
print("Percentage in Math", percentage_Math)
print("Percentage in EE", percentage_EE)
print()

print("Percentage in all subjects:", all_subject_percentage)
