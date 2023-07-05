import math

side1 = 5
side2 = 4
side3 = 3


if side1 == math.sqrt(side2**2 + side3**2):
    print("Triangle is Right Angled")
elif side2 == math.sqrt(side1**2 + side3**2):
    print("Triangle is Right Angled")
elif side3 == math.sqrt(side1**2 + side2**2):
    print("Triangle is Right Angled")
else:
    print("Triangle is NOT Right Angled")
