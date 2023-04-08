lst1 = [7, 20, 25, 30, 37]
lst2 = [30, 55, 60, 75, 100]
lst3 =[]

def func()
for i in lst2:
    if i % 2 ==0:
        lst3.append(i)


for i in lst1:
    if i % 2 != 0:
        lst3.append(i)
print(lst3)
