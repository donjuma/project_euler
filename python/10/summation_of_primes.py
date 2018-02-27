import math
MAX_PRIMES = 2000000

#def list_factors(x):
#    factors = []
#    d = 2
#    while (x > 1):
#        while (x % d == 0):
#            factors.append(d)
#            x /= d
#        d += 1
#    return factors
#
#
#def find_primes(n):
#    primes = []
#    for i in range(n):
#        if (i != 2) and (i % 2 != 0):
#            if len(list_factors(i)) == 1:
#                primes.append(i)
#    return primes
#
#print sum(find_primes(MAX_PRIMES))

def isPrime(num):
    if num < 2:
        return False

    if num > 2 and (num % 2 == 0):
        return False

    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

count = 0
for i in range(2000000):
    if isPrime(i):
        count += i
print count
