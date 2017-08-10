def extended_gcd(x, y):
    if y == 0:
        return (x, 1, 0)
    else:
        d, a, b = extended_gcd(y, x % y)
    return d, b, a - ((x // y) * b)


print(extended_gcd(16 ,10))
