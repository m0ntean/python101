name = 'Neo'
age = 23
print('%s is %7.2f years old' % (name, age))
print('{} is {:7.2f} years old'.format(name, age))
print(f'{name} is {age:7.2f} years old')
bags = 3
bananas_in_bag = 7
print(f'There are total of {bags* bananas_in_bag} bananas')
user = {'name': 'John Roy', 'occupation': 'engineer'}
print(type(user))
x = 5
while x > 0:
    print('Positive')
    x =x-1

count = 0
while count <= 0:
    print(count)
    count = count+1

x = 'Python'
while x:
    print(x)
    x=x[1:]

answer = 'no'
while answer == 'no':
    answer = input("yes or no?")