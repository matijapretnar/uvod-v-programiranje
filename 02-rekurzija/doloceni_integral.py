import math

def veckrat_koreni(x, n):
    """Izračuna √√...√x kjer korenimo n-krat"""
    return veckrat_koreni(math.sqrt(x), n - 1) if n > 0 else x

def uporabi_veckrat(f, x, n):
    """Izračuna f(f(...(f(x))...)) kjer f uporabimo n-krat"""
    return uporabi_veckrat(f, f(x), n - 1) if n > 0 else x

def sestej_vrednosti(f, m, n):
    """Vrne vsoto f(m) + f(m + 1) + ... + f(n - 1)"""
    if m == n:
        return 0
    else:
        k = (m + n) // 2
        return sestej_vrednosti(f, m, k) + f(k) + sestej_vrednosti(f, k + 1, n)

def povrsina_pravokotnika(f, x, eps):
    return f(x) * eps

def vsota_povrsin_pravokotnikov(f, x, eps, n):
    return sestej_vrednosti(lambda i: f(x + i * eps) * eps, 0, n)

def integriraj(f, a, b, n=1000):
    eps = (b - a) / n
    return vsota_povrsin_pravokotnikov(f, a, eps, n)

def poisci_niclo(f, a, b, eps=1e-6):
    c = (a + b) / 2
    if b - a < eps:
        return c
    elif f(a) * f(c) > 0:
        return poisci_niclo(f, c, b, eps)
    else:
        return poisci_niclo(f, a, c, eps)