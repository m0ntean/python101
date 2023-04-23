def func(x):
    y = str(x)
    z = 0
    for i in y:
        if i.isdigit() is True:
            z = z + 1
    return z


a = func(123)
b = func(3.14)
print(a, b)
