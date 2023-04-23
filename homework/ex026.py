

def primes(a, b):
    for i in range(a, b + 1):
        for j in range(2, i ):
            if i % j == 0:
                break
        else:        
            print(i)

primes(25, 50)


def primes2(a, b):
    for i in range(a, b + 1):
        isprime = True
        for j in range(2, i ):
            if i % j == 0:
                isprime = False
                break
        if isprime:        
            print(i)

primes2(25, 50)