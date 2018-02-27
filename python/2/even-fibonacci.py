

i = 2
prev = 1
fib = 0
count = 2
print prev
print i

while(fib < 4000000):
    fib = i + prev
    prev = i
    i = fib
    if (fib % 2 == 0):
        count += fib
#    print fib

print "Sum: " + str(count)

