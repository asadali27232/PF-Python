import math


def caomputeRadius(c1, c2, p1, p2):
    radius = math.sqrt((c2 - c1) ** 2 + (p2 - p1) ** 2)
    return radius


c1 = 0
c2 = 0

p1 = 0
p2 = 0

c1, c2 = tuple(input("Enter center points c1 c2").strip().split())
p1, p2 = tuple(input("Enter center points p1 p2").strip().split())

radius = caomputeRadius(c1, c2, p1, p2)
