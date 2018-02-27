from collections import Counter

factors = []

def factor(x):
    d = 2
    local_factors = []
    while(x > 1):
        while(x % d == 0):
            local_factors.append(d)
            x /= d
        d += 1
    return local_factors

for i in range(21):
    factors += list((Counter(factor(i))-Counter(factors)).elements())

print reduce(lambda x, y: x*y, factors)
