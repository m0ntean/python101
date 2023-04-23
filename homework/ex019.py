def func(string, sub_string):
    x = string.split()
    z = 0

    for i in x:
        if sub_string == i:
            z = z + 1
    return z

x = "Neo is good developer. Neo is a writer"
y = 'Neo'
y = func(x, y)
print(y)