slovar_stevil = {}

def stevilo_stolpov1(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif n in slovar_stevil:
        return slovar_stevil[n]
    else:
        spodaj_modra_1 = stevilo_stolpov1(n - 1)
        spodaj_rdeca_2 = stevilo_stolpov1(n - 2)
        spodaj_zelena_3 = stevilo_stolpov1(n - 3)
        skupaj = spodaj_modra_1 + spodaj_rdeca_2 + spodaj_zelena_3
        slovar_stevil[n] = skupaj
        return skupaj


def memoiziraj(f):
    rezultati = {}
    def mem_f(x):
        if x not in rezultati:
            rezultati[x] = f(x)
        return rezultati[x]
    return mem_f

def stevilo_stolpov2(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        spodaj_modra_1 = stevilo_stolpov2(n - 1)
        spodaj_rdeca_2 = stevilo_stolpov2(n - 2)
        spodaj_zelena_3 = stevilo_stolpov2(n - 3)
        return spodaj_modra_1 + spodaj_rdeca_2 + spodaj_zelena_3

stevilo_stolpov2 = memoiziraj(stevilo_stolpov2)

@memoiziraj
def stevilo_stolpov3(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        spodaj_modra_1 = stevilo_stolpov3(n - 1)
        spodaj_rdeca_2 = stevilo_stolpov3(n - 2)
        spodaj_zelena_3 = stevilo_stolpov3(n - 3)
        return spodaj_modra_1 + spodaj_rdeca_2 + spodaj_zelena_3

from functools import lru_cache

@lru_cache(maxsize=None)
def stevilo_stolpov4(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        spodaj_modra_1 = stevilo_stolpov4(n - 1)
        spodaj_rdeca_2 = stevilo_stolpov4(n - 2)
        spodaj_zelena_3 = stevilo_stolpov4(n - 3)
        return spodaj_modra_1 + spodaj_rdeca_2 + spodaj_zelena_3

