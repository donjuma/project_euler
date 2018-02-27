SUM = 1000
integers = range(1,1001)
intLen = len(integers)
aRange = intLen/3
bRange = ((intLen - aRange) / 2) + aRange

for a in range(1, aRange):
    for b in range(aRange+1, bRange):
        c = SUM - a - b
        if (a*a) + (b*b) == (c*c):
            print a,b,c
            print a*b*c

