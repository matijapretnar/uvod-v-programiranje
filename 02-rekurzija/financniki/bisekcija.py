def bisekcija(f, a, b, eps=1e-10):
    assert f(a) * f(b) < 0
    c = (a + b) / 2
    if b - a < eps:
        return c
    elif f(c) == 0:
        return c
    elif f(a) * f(c) < 0:
        return bisekcija(f, a, c)
    else:
        return bisekcija(f, c, b)
