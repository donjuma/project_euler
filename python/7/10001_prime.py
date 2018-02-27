

primes = []

def calculate_factors(n):
    factors = []
    d = 2
    while n > 1:
        while (n % d == 0):
            factors.append(d)
            n /= d
        d += 1
    return factors

def check_primes(max):
    i = 2
    while (len(primes) < max):
        if len(calculate_factors(i)) == 1:
            primes.append(i)
        i += 1

check_primes(10001)
print primes[len(primes)-1]
