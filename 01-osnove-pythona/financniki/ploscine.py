def ploscina_trikotnika(a, b, c):
    '''Izračuna ploščino trikotnika z danimi stranicami.'''
    s = (a + b + c) / 2
    ploscina = (s * (s - a) * (s - b) * (s - c)) ** (1 / 2)
    return ploscina


def povrsina_tetraedra(a, b, c, d, e, f):
    '''Izračuna površino tetraedra z danimi stranicami.'''
    povrsina = 0
    povrsina = povrsina + ploscina_trikotnika(a, b, c)
    povrsina = povrsina + ploscina_trikotnika(a, e, f)
    povrsina = povrsina + ploscina_trikotnika(b, d, f)
    povrsina = povrsina + ploscina_trikotnika(c, d, e)
    return povrsina


a = 4
b = 13
c = 15
d = 8
e = 12
f = 9

s_abc = (a + b + c) / 2
ploscina_abc = (s_abc * (s_abc - a) * (s_abc - b) * (s_abc - c)) ** (1 / 2)
s_aef = (a + e + f) / 2
ploscina = (s_aef * (s_aef - a) * (s_aef - e) * (s_aef - f)) ** (1 / 2)
s = (a + b + c) / 2
ploscina = (s * (s - a) * (s - b) * (s - c)) ** (1 / 2)
s = (a + b + c) / 2
ploscina = (s * (s - a) * (s - b) * (s - c)) ** (1 / 2)
