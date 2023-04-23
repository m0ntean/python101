def func(x):

    y = str(x)
    if y == y[::-1]:
        return True
    else:
        return False


x = func(543)
print(x)