def koren(n):
    a, b = 0, n
    while b - a > 1e-1000:
        print(a, b)
        c = (a + b) / 2
        if c * c >= n:
            b = c
        else:
            a = c
    return c
