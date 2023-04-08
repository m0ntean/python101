

def bounce(h):
    y = list(range(1,11))
    for i in y:
        x = h * 3/5
        h = x
        x=round(x,2)
        print(i,x)


bounce(1000)


