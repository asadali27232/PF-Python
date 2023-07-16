import math

def computeStat(x1, x2, x3, x4, x5):
    x = (x1 + x2 + x3 + x4 + x5) / 5
    s = math.sqrt(((x1-x)**2 + (x2-x)**2 + (x3-x)**2 + (x4-x)**2 + (x5-x)**2) / 5)
    return x, s

mean, stanDev = computeStat(1,2,3,4,5)

print(mean, stanDev)