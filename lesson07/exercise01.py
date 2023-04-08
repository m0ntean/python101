keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
x=dict()
print(len(keys))
for i in range(len(keys)):
    y = keys[i]
    z = values[i]
    print(i, y, z)
    x[y] = z
print(x)