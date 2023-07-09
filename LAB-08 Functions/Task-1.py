import math


def nothing_function():
    pass


def average(a, b, c):
    return (a + b + c) / 3


avg1 = average(2, 6, average(5, 10, 15))
avg2 = average(2, 6, average(math.sqrt(25), 10, 15))
avg3 = round(average(2, 7, 1), 2)

print(avg1, avg2, avg3)


def my_sum(a, b, c):
    return a + b + c
    return (a + b + c) / 3


sum1 = my_sum(2, 6, my_sum(5, 10, 15))
sum2 = my_sum(2, 6, my_sum(math.sqrt(25), 10, 15))
sum3 = round(my_sum(2, 7, 1), 2)

print(sum1, sum2, sum3)


def average(a, b, c):
    print((a + b + c) / 3)


avg1 = average(2, 6, 8)
avg2 = average(2, 6, 6)
avg3 = average(2, 7, 1)

print(avg1, avg2, avg3)


def larger_char(a, b):
    if a > b:
        print(a)
    else:
        print(b)


larger_char("c", "r")
larger_char("c", "A")
