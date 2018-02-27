

MAX = 1000
summation = 0

for i in xrange(MAX):
    if (i % 5 == 0) or (i % 3 == 0):
        summation += i

print summation
