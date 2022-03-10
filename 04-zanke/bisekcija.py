def koren(n, k=2, eps=1e-10):
    a = 0
    b = n
    while b - a > eps:
        c = (a + b) / 2
        print(f"{c} ∈ [{a}, {b}]")
        print(f"{c}^{k} = {c ** k}")
        if c ** k < n:
            a = c
        else:
            b = c
    return c


import math

def nicla_sinusa(a, b, eps=1e-10):
    while b - a > eps:
        c = (a + b) / 2
        if math.sin(c) * math.sin(a) > 0:
            a = c
        else:
            b = c
    return c


def nicla(f, a, b, eps=1e-10):
    while b - a > eps:
        c = (a + b) / 2
        if f(c) * f(a) > 0:
            a = c
        else:
            b = c
    return c
