# num = int(input("Enter a single digit number (0-9): "))
num = 3
match num:
    case 0:
        print("Zero")
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case 4:
        print("Four")
    case 5:
        print("Five")
    case 6:
        print("Six")
    case 7:
        print("Seven")
    case 8:
        print("Eight")
    case 9:
        print("Nine")
    case _ if num > 9 and not num < 0:
        print("Number is greater than 9. Enter between 0 and 9.")
    case _:
        print("Invalid Input...!")
