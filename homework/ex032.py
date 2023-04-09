x = open('/home/monte/python101/homework/test.txt', 'r')
y =x.readlines()
print(y[3].strip())
x.close()