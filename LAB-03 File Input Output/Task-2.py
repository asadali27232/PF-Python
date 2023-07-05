sec = int(input("Enter time seconds: "))

hours = (sec // 60) // 60
minutes = (sec - (hours * 60 * 60)) // 60
sec = sec - (minutes * 60) - (hours * 60 * 60)

print("{:>2}:{:>2}:{:>2}".format(hours, minutes, sec))
