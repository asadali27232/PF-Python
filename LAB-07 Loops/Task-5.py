num1 = int(input(("Enter First Number: ")))
num2 = int(input(("Enter Second Number: ")))

sum = 0

for i in range(num1, num2 + 1):
    if i % 2 == 0:
        sum += i

print("Sum of even number between given range: ", sum)
