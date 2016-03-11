def gcd(m, n):
    '''Izračuna največji skupni delitelj števil m in n.'''
    while n > 0:
        m, n = n, m % n
    return m

gcd(456, 123)

def bisekcija(f, a, b, eps=1e-10):
    assert f(a) * f(b) < 0
    while b - a > eps:
        c = (a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return b

import math
bisekcija(math.cos, 0, 2)