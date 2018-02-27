

def check_even_divisible(x):
    for i in range(1, 20):
        if x % i != 0:
            return False
    return True

multiple = 1

while not check_even_divisible(multiple):
    multiple += 1
print multiple
