
max = 600851475143

def factorize(n):
    d = 2
    factors = []
    while (n > 1):
        while(n % d == 0):
            factors.append(d)
            n /= d
        d += 1
    return factors

factors =factorize(max)

highest = 0
for i in factors:
    if i > highest:
        highest = i
print highest
