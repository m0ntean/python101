def f(s):
    d = ''
    z = s.split()
    for w in z:
        print(w[0])
        d +=w[0].upper()
    return d

x = 'To be honest'
y = f(x)
print(y)
