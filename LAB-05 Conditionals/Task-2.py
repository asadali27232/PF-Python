x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))

count = 0
for i in [x, y, z]:
    if i >= 0:
        count += 1
print(count)
