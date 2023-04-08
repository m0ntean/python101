import math

def hyp(a, b):
    
    c = math.sqrt(a**2 + b**2)
    return c

a = 4
b = 3
x = hyp(a, b)
print(x)