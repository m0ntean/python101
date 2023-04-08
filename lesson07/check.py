grades = 2, 3, 4
print(type(grades))
print(grades[0])
print(len(grades))
print(grades[-1])
for grade in grades:
    print(grade)

tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
print(tuple1[1][1])

sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]
x = set(sample_list)
y = x | sample_set
print(y)

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
x = set1 & set2
print(x)