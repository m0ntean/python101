def isprime(x):
    for i in range(2, x ):
        if x % i == 0:
            return False
    return True

y = isprime(25)
print(y)