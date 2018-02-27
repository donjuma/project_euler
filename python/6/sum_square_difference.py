
value = 100

def sumOfSquares(x):
    summ = 0
    for i in range(x+1):
        summ += (i*i)
    return summ


def squareOfSums(x):
    square = 0
    for i in range(x+1):
        square += i
    square *= square
    return square


print (squareOfSums(value) - sumOfSquares(value))
