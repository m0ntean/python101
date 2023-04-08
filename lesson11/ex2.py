

def factorial(num):
    x = 1
    for i in range(1,num + 1):
        x = x * i
        print(x)
    return x

y = factorial(5)
print(y)

x = b'Python, bytes \xd5\xa1\xd5\xb5\xd5\xb8'
print(len(x))
print(type(x))
print(x.decode())
y = bytes('Python, bytes այո', 'utf8')
print(y)

z = ord(b'\xd5\xa1'.decode())
print(z)

print(chr(1377))