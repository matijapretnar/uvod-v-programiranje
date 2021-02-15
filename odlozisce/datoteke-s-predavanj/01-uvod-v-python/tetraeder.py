def ploscina_trikotnika(a, b, c):
    s = (a + b + c) / 2
    # sedaj uporabimo Heronov obrazec
    ploscina = (s * (s - a) * (s - b) * (s - c)) ** (1 / 2)
    return ploscina

def povrsina_tetraedra(a, b, c, d, e, f):
    p_abc = ploscina_trikotnika(a, b, c)
    p_aef = ploscina_trikotnika(a, e, f)
    p_dbf = ploscina_trikotnika(d, b, f)
    p_dec = ploscina_trikotnika(d, e, c)
    return p_abc + p_aef + p_dbf + p_dec
