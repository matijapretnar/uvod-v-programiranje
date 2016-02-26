import math


def ploscina_trikotnika(a, b, c):
    '''Vrne ploščino trikotnika z danimi stranicami.'''
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def povrsina_tetraedra(a, b, c, d, e, f):
    '''Vrne površino tetraedra z danimi stranicami.'''
    povrsina = 0
    povrsina += ploscina_trikotnika(a, b, c)
    povrsina += ploscina_trikotnika(a, e, f)
    povrsina += ploscina_trikotnika(b, d, f)
    povrsina += ploscina_trikotnika(c, d, e)
    return povrsina

