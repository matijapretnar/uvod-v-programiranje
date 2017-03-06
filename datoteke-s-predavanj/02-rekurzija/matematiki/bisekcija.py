def bisekcija(f, a, b, eps=1e-8):
    '''Vrne ničlo funkcije f na intervalu [a, b].'''
    assert f(a) * f(b) < 0
    c = (a + b) / 2
    if b - a < eps:
        return c
    if f(a) * f(c) < 0:
        return bisekcija(f, a, c)
    else:
        return bisekcija(f, c, b)

def moja_funkcija(x):
    return x - 2