def gcd(m, n):
    '''Vrne največji skupni delitelj števil m in n.'''
    while n > 0:
        m, n = n, m % n
    return m

def bisekcija(f, a, b, eps=1e-8):
    '''Vrne ničlo funkcije f na intervalu [a, b].'''
    assert f(a) * f(b) < 0
    while b - a > eps:
        c = (a + b) / 2
        if f(b) * f(c) < 0:
            a = c
        else:
            b = c
    return a

import math
bisekcija(math.sin, 2, 4)
