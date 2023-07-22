numbers = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

_2x15 = [numbers[0:15], numbers[15:]]
print(_2x15)

_3x10 = [numbers[0:10], numbers[10:20], numbers[20:]]
print(_3x10)

_6x5 = [numbers[0:5], numbers[5:10], numbers[10:15], numbers[15:20], numbers[20:25], numbers[25:]]
print(_6x5)

table_of_numbers = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]

last_element = table_of_numbers[-1][-1]
print(last_element)

table_of_numbers[2][-2] = 55
print(table_of_numbers)

print(table_of_numbers[2])

for i in range(4):
    print(table_of_numbers[i][-1])

for row in table_of_numbers:
    for column in row:
        print(column)

A = [[], [], []]
for i in range(3):
    for j in range(3):
        A[i].append(int(input(f"Enter A[{i}][{j}] ")))

print(A)
print(sum(A[0]) + sum(A[1]) + sum(A[2]))

sum = [[], [], []]
for i in range(3):
    for j in range(3):
        sum[i].append(A[i][j] + A[i][j])
print(sum)
