while True:
    N = int(input("Enter N: "))
    if N > 0:
        break

for i in range(1, N + 1):
    for ii in range(1, i + 1):
        print("*", end="")
    print()
print()

for j in range(N, 0, -1):
    for jj in range(1, j + 1):
        print("*", end="")
    print()
print()

for k in range(1, N + 1):
    for kk in range(1, N + 1):
        if kk < k:
            print(" ", end="")
        else:
            print("*", end="")
    print()
print()

for l in range(N, 0, -1):
    for ll in range(1, N + 1):
        if ll < l:
            print(" ", end="")
        else:
            print("*", end="")
    print()
print()
