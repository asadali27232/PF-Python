import math


def caomputeRadius(c1, c2, p1, p2):
    c1 = int(c1)
    c2 = int(c2)
    p1 = int(p1)
    p2 = int(p2)
    radius = math.sqrt((c2 - c1) ** 2 + (p2 - p1) ** 2)
    return radius


def circle_stats(radius):
    area = math.pi * radius**2
    circumference = 2 * math.pi * radius
    return area, circumference


c1 = 0
c2 = 0

p1 = 0
p2 = 0

c1, c2 = tuple(input("Enter center points c1 c2: ").strip().split())
p1, p2 = tuple(input("Enter center points p1 p2: ").strip().split())

radius = caomputeRadius(c1, c2, p1, p2)
print("Radius is: ", radius)
print("Area and circumference are: ", circle_stats(radius))
