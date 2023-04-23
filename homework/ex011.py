def cut_chars(s, n):

    return s[-n:]
    

x = cut_chars("abcde", 4)
print(x)  # bcde


x = cut_chars("thisisit", 2)
print(x)  # it
