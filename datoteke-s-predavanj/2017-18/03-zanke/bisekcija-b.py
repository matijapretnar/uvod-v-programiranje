def koreni(n, eps=1e-12):
    a, b = 0, max(1, n)
    while b - a > eps:
        # print(a, b)
        c = (a + b) / 2
        if c * c > n:
            b = c
        else:
            a = c
    return (a + b) / 2

def poisci_niclo(f, a, b, eps=1e-12):
    while b - a > eps:
        print(a, b)
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

def moj_polinom(x):
    return x ** 3 - 3 * x ** 2 + 3 * x - 1

def moja_kvadratna_funkcija(x):
    return x ** 2 - 10