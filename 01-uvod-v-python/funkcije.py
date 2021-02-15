def ploscina_trikotnika(a, b, c):
    s = (a + b + c) / 2
    ploscina = (s * (s - a) * (s - b) * (s - c)) ** (1 / 2)
    return ploscina

def povrsina_ikozaedra(a):
    return 20 * ploscina_trikotnika(a, a, a)

def predznak(x):
    if x < 0:
        return -1
    else:
        if x > 0:
            return 1
        else:
            return 0

def predznak(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    else:
        return 0

def dva_returna(x):
    return x + 20
    return x + 100

def nic_returnov(x):
    x + 20

def fakulteta(n):
    if n == 0:
        return 1
    else:
        return n * fakulteta(n - 1)
