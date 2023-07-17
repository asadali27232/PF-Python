import math


def f(x):
    return math.sqrt(4 - math.pow(x, 2))


def trap(a, b, n):
    h = (b - a) / n
    s = f(a) + f(b)
    inter = a
    for _ in range(1, n):
        inter = inter + h
        s += 2 * f(inter)
    return s * h / 2


integral = trap(0, 2, 100)
print(round(integral), 2)
