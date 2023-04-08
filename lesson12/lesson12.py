def is_sorted(num_list):

    length = len(num_list)
    indexes = list(range(length - 1))
    for i in indexes:
        if num_list[i] > num_list[i + 1]:
            return False
    return True


lst = [1, 2 ,3, 4]
y = is_sorted(lst)
print(y)