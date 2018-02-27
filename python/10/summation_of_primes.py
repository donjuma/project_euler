import math
MAX_PRIMES = 2000000

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
