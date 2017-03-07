def ploscina_trikotnika(a, b, c):
    s = (a + b + c) / 2
    ploscina = (s * (s - a) * (s - b) * (s - c)) ** (1 / 2)
    return ploscina

def povrsina_tetraedra(a, b, c, d, e, f):
    return (
        ploscina_trikotnika(a, b, c)
        + ploscina_trikotnika(a, d, e)
        + ploscina_trikotnika(b, e, f)
        + ploscina_trikotnika(c, d, f)
    )

def absolutna_vrednost(x):
    if x >= 0:
        return x
    else:
        return -x

def fakulteta(n):
    if n == 0:
        return 1
    else:
        return n * fakulteta(n - 1)

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
