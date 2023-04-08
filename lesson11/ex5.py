z = [1, 2, 3, 4, 5]


def sum(lst):
    """ Calculate sum of list elements
    >>> sum([1, 2])
    3
    """
    x = 0
    for i in lst:
        x += i
        print(x)
    return x

y = sum(z)
print(y)
print(help(sum))