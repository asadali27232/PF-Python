# [sentinel-controlled loop]

number = int(input("Enter number: "))

sumOdd = 0
sumEven = 0

while number != -1:
    if number > 0:
        if number % 2 == 0:
            sumEven += number
        else:
            sumOdd += number
    number = int(input("Enter number: "))
    
print("Sum of even numbers is: ", sumEven)
print("Sum of odd numbers is: ", sumOdd)
