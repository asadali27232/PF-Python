sum = []


def sum_arrays(A, B):
    global sum
    for i in range(len(A)):
        sum.append(A[i] + B[i])
    return sum


A = [1, 2, 3, 4, 5]
B = [3, 4, 5, 6, 10]

print(sum_arrays(A, B))
print(A)
print(B)
print(sum)
