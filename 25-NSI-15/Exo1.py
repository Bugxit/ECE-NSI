def multiplication(n1, n2):
    res = 0
    abs_n1 = n1 if n1 > 0 else -n1
    abs_n2 = n2 if n2 > 0 else -n2
    x = 0
    while x < abs_n2:
        res += abs_n1
        x += 1

    if (n1 < 0) ^ (n2 < 0):
        res = -res

    return res

print(multiplication(3, 5))
print(multiplication(-4,-8))
print(multiplication(-2, 6))
print(multiplication(-2, 0))
