import math

def f1(x):
    return x ** 2 - 2

def f2(x):
    return x ** 3 - 8

def f3(x):
    return (x - 5) * (x - 2) * (x - 11)

def poisci_niclo(f, a, b):
    assert f(a) * f(b) <= 0
    while b - a > 1e-10:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c

# poisci_niclo(0, 4)
