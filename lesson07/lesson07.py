employee = {
'864-20': ['Arm', 'Sia'],
'987-65': ['Vlad', 'Noa'],
'100-01': ['Kia', 'Yan']}
print(employee)
print(employee['864-20'])
employee['864-20'] = ['Inga', 'Nord']
print(employee)
print(employee['864-20'])
emptydict = dict()
print(emptydict)

days = {'Mo':1, 'Tu':2, 'W':3}
print(days['Mo'])
print(days['Tu'])
days['Th'] = 4
print(days)
print('Fr' in days)
print(len(days))
print(list(days.items()))
print(list(days.keys()))
print(days.pop('Mo'))
print(days)
print(days.update(employee))
print(days)
values = days.values()
print(values)

for value in values:
    print(value)

