import math

a = 3
b = 3
c = 3
d = 2
e = 2
f = 2


def ploscina_trikotnika(a, b, c):
    """Vrne ploščino trikotnika z danimi stranicami"""
    # Za izračun ploščine uporabimo Heronovo formulo
    # https://sl.wikipedia.org/wiki/Heronova_formula
    s = (a + b + c) / 2
    ploscina = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return ploscina
    # Lahko bi napisali tudi
    # return math.sqrt(s * (s - a) * (s - b) * (s - c))
    # ampak je zgornja verzija bolj natančno razčljenjena


def povrsina_tetraedra(a, b, c, d, e, f):
    ploscina_abc = ploscina_trikotnika(a, b, c)
    ploscina_aef = ploscina_trikotnika(a, e, f)
    ploscina_dbf = ploscina_trikotnika(d, b, f)
    ploscina_dec = ploscina_trikotnika(d, e, c)
    return ploscina_abc + ploscina_aef + ploscina_dbf + ploscina_dec
