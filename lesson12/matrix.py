lst = [[3,5,7,8], [0,2,1,6], [3,8,3,1]]

def print2d(t):
    for i in t:
        for j in i:
            print(j, end=' ')
        print()
print2d(lst)


def incr2d(t):
    for i in t:
        for j in i:
            x = j + 1
            print(x, end=' ')
        print()

#incr2d(lst)
        

def incr2dx(t):
    nrows = len(t)
    ncols = len(t[0])

    for i in range(nrows):
        for j in range(ncols):
            t[i][j] += 1

incr2dx(lst)
print2d(lst)
