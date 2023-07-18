input_file = open("C:\Users\LENOVO\Repos\PF-Python\LAB-03 File Input Output\input.txt", "r")
input_file_content = input_file.read()
input_lines = input_file_content.split("\n")

output_lines = []

for emp in input_lines:
    emp_details = emp.split()
    increased_salary = str(
        int(emp_details[2]) + (int(emp_details[2]) * int(emp_details[3]) / 100)
    )
    emp_details_updated = [emp_details[0], emp_details[1], increased_salary]

    output_lines.append(" ".join(emp_details_updated))

output_file_content = "\n".join(output_lines)
output_file = open("output.txt", "w")
output_file.write(output_file_content)
