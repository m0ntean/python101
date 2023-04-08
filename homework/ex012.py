lst = [10, 20, 33, 46, 55]

def func(x):
    new_lst = []
    for i in x:
        if i % 5 == 0:
            new_lst.append(i)
    return new_lst


y = func(lst)
print(y)


