def modExp(x, y, m):
    print(x, y, m)
    if y == 0:
        return 1
    else:
        z = modExp(x, y // 2, m)
        if  y % 2 == 0:
            return z * z % m
        else:
            return x * z * z % m

print(modExp(5, 3, 13))
