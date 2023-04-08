data = [1,2,3,4,5]


for i in data:
    print(i)

name = 'Apple'
for char in name:
    print(char)

for word in ['stop','desktop','post','top']:
    if'top' in word:
        print(word)
print('done')        

print(list(range(0, 5)))
print(list(range(10, 20)))

for i in list(range(2,46,10)):
    print(i)

print(list(range(1, 10)))   
print(list(range(0,9,2)))
print(list(range(1,10,2)))
print(list(range(20,61,10)))

print(list(range(100, 4,-1)))

y=0
for x in list(range(5,61,1)):
    y=x+y
print(y)

b=1
for a in list(range(5,31,1)):
    
    if a%7==0:
        b=a*b
print(b)

for letter in 'Python':
    if letter == 'h':
        continue
    print('Curremt Letter:', letter)    