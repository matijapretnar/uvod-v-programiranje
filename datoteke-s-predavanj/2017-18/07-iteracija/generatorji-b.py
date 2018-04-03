import time

def en_dva_tri_v_nedogled():
    while True:
        yield 1
        yield 2
        yield 3

def zaciklaj(iterable):
    while True:
        yield from iterable


def stopaj(f):
    def f_s_casom(*args, **kwargs):
        zacetek = time.time()
        y = f(*args, **kwargs)
        konec = time.time()
        print('Porabil sem {} sekund'.format(konec - zacetek))
        return y
    return f_s_casom

def razpon_s_seznami(m, n):
    seznam = []
    while m < n:
        seznam.append(m)
        m += 1
    return seznam

def razpon_z_vnaprej_pripravljenimi_seznami(m, n):
    seznam = (n - m) * [None]
    i = 0
    while m + i < n:
        seznam[i] = m + i
        i += 1
    return seznam

def razpon_z_generatorji(m, n):
    while m < n:
        yield m
        m += 1

@stopaj
def neumna_vsota(m, n):
    vsota = 0
    for x in razpon_s_seznami(m, n):
        vsota += x
    return vsota

@stopaj
def pametna_vsota(m, n):
    vsota = 0
    for x in razpon_z_generatorji(m, n):
        vsota += x
    return vsota

def delitelji(n):
    druga_polovica = []
    for d in range(1, int(n ** 0.5) + 1):
        if n % d == 0:
            yield d
            druga_polovica.append(n // d)
    druga_polovica_v_pravem_vrstnem_redu = reversed(druga_polovica)
    if druga_polovica[-1] ** 2 == n:
        next(druga_polovica_v_pravem_vrstnem_redu)
    yield from druga_polovica_v_pravem_vrstnem_redu

# {n ** 2 | n = 1...10}

def seznam_kvadratov(seznam):
    kvadrati = []
    for x in seznam:
        kvadrati.append(x ** 2)
    return kvadrati

def seznam_kvadratov(seznam):
    return [x ** 2 for x in seznam]

def identicna_matrika(n):
    return [
        [1 if i == j else 0 for j in range(n)]
        for i in range(n)
    ]
