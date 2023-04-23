def double_value(value):
    return value + value

x = double_value(5)
y = double_value("abc")
z = double_value([1,2,3])

print(x, y, z, sep='\n')