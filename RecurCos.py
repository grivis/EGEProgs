import math

x = 3.14
n = 5

def recos(x, n):
    if n <=1:
        return math.cos(x)
    else:
        return math.cos(x**n) + recos(x, n-1)

print(recos(x, n))
