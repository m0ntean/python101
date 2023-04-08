# x=5+30*20//10
# print(x)
# s = 'rock'
# print(s)
# t = 'climbing'
# s == 'rock'
# print(t)
# print(s != t)
# print(s < t)
# print(s > t)
# print(s + t)
# print(s + ' '+ t)
# print(3 * s)
# print(ord('b'))
# print(3 * '_')
# print('o' in s)
# print('bi' in t)
# print('o' in t)
# print(len(t))
# pets = ['ant', 'bat', 'cod', 'dog', 'elk']
# pets[2]='cow'
# print(pets)
# pet = 'cod'
# #pet[-1]='w'
# print(pet)
# lst = [1, 1, 3]
# print(len(lst))
# lst.append(5)
# print(lst)
# print(lst.count(1))
# print(lst.index(3))
# print(lst.pop())
# print(lst.remove(3))
# print(lst)

# lst = [159.99, 160.00, 205.95,128.83, 175.49]
# lst.append(160)
# print(lst)
# print(lst.count(160))
# print(min(lst))
# print(lst.index(128.83))
# print(lst.remove(128.83))
# print(lst)
# print(lst.sort())
# print(lst)

excuse = "I'm\n \"s\tick\""
print(excuse)

x = '''"What's up guys" 
said Robert'''
print(x)
s = 'Apple'
print(s[0:2])
print(s[1:4])
print(s[2:5])
print(s[2:])
print(s[-3:-1])
print(s[:2])

days = ['Sun', 'Mon', 'Tue', 'Wed','Thur', 'Fri', 'Sat']
middle_days = days[2:5]
print(middle_days)
numbers = [1,2,3,4,5]
print(numbers[1:3])
print(numbers[:3])
print(numbers[3:])
numbers_copy = numbers
print(id(numbers_copy),id(numbers))
del numbers[1:3]
print(numbers)

lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(lst[0:4])
print(lst[3:6])
print(lst[-5:-4])
print(lst[-3:-1])
print(lst[3:])
print(lst[-3:])

s = 'apple is good'
t= 'pp'
sep= ' '
print(s.capitalize())
print(s.count(t))
print(s.find(t))
print(s.lower())
print(s.replace('p','y'))
print(s.split(sep))
print(s.upper())
link='http://www.main.com/smith/index.html'
link2=link.split('/')
print(link2)

events = '9/13 2:30 PM\n9/14 11:15 AM\n9/14 1:00 PM\n9/15 9:00 AM'
print(events)
i1=events.find('9/14')
i3=events.find('9/15')
print(events[i1:i3].strip().split('\n'))
