import math


def ploscina_trikotnika(a, b, c):
    s = (a + b + c) / 2
    ploscina = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return ploscina


def povrsina_ikozaedra(a):
    return 20 * ploscina_trikotnika(a, a, a)


ploscina = ploscina_trikotnika(4, 13, 15) + ploscina_trikotnika(3, 4, 5)
