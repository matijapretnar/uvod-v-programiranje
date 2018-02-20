import math


def ploscina_trikotnika(a, b, c):
    # Uporabili bomo Heronov obrazec
    # (https://sl.wikipedia.org/wiki/Heronova_formula)
    s = (a + b + c) / 2
    ploscina = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return ploscina


def povrsina_tetraedra(a, b, c, d, e, f):
    p_abc = ploscina_trikotnika(a, b, c)
    p_aef = ploscina_trikotnika(a, e, f)
    p_bdf = ploscina_trikotnika(b, d, f)
    p_cde = ploscina_trikotnika(c, d, e)
    return p_abc + p_aef + p_bdf + p_cde


def dva_returna(x):
    return x ** 2
    return 1 / 0


def brez_returna(x):
    x ** 2


def f(x):
    y = 3 * x
    return y


def absolutna_vrednost(x):
    if x < 0:
        return -x
    else:
        return x


def predznak(x):
    if x < 0:
        return -1
    elif x == 0:
        return 0
    else:
        return 1
