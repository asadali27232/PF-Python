n = int(input("Enter N: "))

zeros = 0
positive = 0
negative = 0

for i in range(n):
    number = int(input("Enter a number: "))
    if number == 0:
        zeros += 1
    elif number > 0:
        positive += 1
    elif number < 0:
        negative += 1

print("You Entered {} zeros".format(zeros))
print("You Entered {} positive numbers".format(positive))
print("You Entered {} negative numbers".format(negative))
