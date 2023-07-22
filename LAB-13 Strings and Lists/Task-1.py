str1 = []
str2 = []

str1 = list("Sunny Day")
str1_len = len(str1)

name = list("ABCDEFGHIJKL")
str2 = name.copy()
str2_len = len(str2)

print(str1) if str1_len > str2_len else print(str2)
