while True:
    N = int(input("Enter N: "))
    if N > 0:
        break

for i in range(1, N + 1):
    while True:
        T = int(input("Enter T: "))
        if T > 0:
            break

    for i in range(1, 11):
        print("{:>2} x {:>2} = {:>2}".format(T, i, T * i))
