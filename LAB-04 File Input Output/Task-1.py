import math

input_file = open("inData.txt", "r")
output_file = open("outData.txt", "w")

width, hieght = tuple(input_file.readline().strip().split())
rect_area = float(width) * float(hieght)
output_file.writelines(
    "\nRectangle: \nWidth = {}, Hieght = {}, Area = {}\n".format(
        width, hieght, round(rect_area, 2)
    )
)

radius = float(input_file.readline())
cir_area = math.pi * radius**2
output_file.writelines("\nCircle:\nRadius = {}, Area = {}\n".format(radius, cir_area))

fname, lname, age = tuple(input_file.readline().strip().split())
output_file.writelines("\nName: {} {}, Age: {}\n".format(fname, lname, age))

balance, rate = tuple(input_file.readline().strip().split())
interest = float(balance) + (float(balance) * float(rate))
output_file.writelines(
    "Current Balanec: {}, Balance at the end of Month: {}".format(balance, interest)
)
