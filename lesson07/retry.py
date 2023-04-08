keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
x = dict()
for i in range(len(keys)):
    key = keys[i]
    value = values[i]
    print(i, key, value)
    x[key] = value
print(x)

y = dict()
w = 2
while w >= -1:
    key = keys[w]
    value = values[w]
    print(w, key, value)
    y[key] = value
    w =w-1
    print(y)