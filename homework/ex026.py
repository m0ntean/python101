def isprime(x):
    for i in range(2, x ):
        if x % i == 0:
            return False
    return True

y = isprime(25)
print(y)

def primes(a, b):
    for i in range(a, b + 1):
        if isprime(i) is True:
            print(i)

primes(25, 50)