prod = 'bread'
cost = 2
wght = 700
total = cost*wght
print(prod, cost, wght, total)
print(prod, cost, wght, total, sep=':')
pets=['boa', 'cat', 'dog']
for pet in pets:
    print(pet)
for pet in pets:
    print(pet, end=',')
print()
for pet in pets:
    print(pet, end=', ')
print()        
for pet in pets:
    print(pet, end='!!!')
print()        

day = 'Wednesday'
month = 'March'
weekday = 'Wednesday'
month = 'March'
day = 10
year = 2010
year = 2012
hour = 11
minute = 45
second = 33
print("hour"+':'+"minute+"':'+"second")
print(str(hour)+':'+str(minute)+':'+str(second))
print('{}:{}:{}'.format(hour, minute, second))
print(f"{hour}:{minute}:{second}")
print(f"{weekday}, {month}, {day}, {year} at {hour}:{minute}:{second}")

for i in range(1, 8):
    print(i, i**2, 2**i)

for i in range(1, 8):
    print('{} {:2} {:3}'.
    format(i, i**2, 2**i))  

lst = ['Jeff Bezos','Tim Cook', 'Larry Ellison']
for name in lst:
    fl = name.split()
    print(fl[0], fl[1])

n = 10
print('{:b}'.format(n))
print(repr('{:c}'.format(n)))
print('{:d}'.format(n))
print('{:x}'.format(n+6))
print('{:e}'.format(n))
print('{:7.2f}'.format(n*100))

file = open('data.txt', 'r')
s = file.read()
file.close()
print(print(s))
