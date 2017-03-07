def bisekcija(f, a, b, eps=1e-10):
    assert f(a) * f(b) < 0
    c = (a + b) / 2
    if b - a < eps:
        return c
    elif f(c) == 0:
        return c
    elif f(a) * f(c) < 0:
        return bisekcija(f, a, c, eps=eps)
    else:
        return bisekcija(f, c, b, eps=eps)

import math
bisekcija(math.cos, 0, 2, eps=1e-3)
