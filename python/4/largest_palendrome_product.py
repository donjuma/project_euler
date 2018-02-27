pals = []

def check_if_palendrome(x):
    x = str(x)
    if x == x[::-1]:
        return True
    else:
        return False

def calculate_products(left, right):
    for i in range(left, 0, -1):
        for j in range(right, 0, -1):
            if check_if_palendrome(i*j):
                pals.append(i*j)

calculate_products(999, 999)
highest = 0
for p in pals:
    if p > highest:
        highest = p
print highest
