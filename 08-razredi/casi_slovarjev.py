import random
import stopaj
from slovarji import Slovar


def nakljucni_pari(n):
    for i in range(n):
        yield (i, random.randint(-i, i))


def poisci(slovar, x):
    return slovar[x]


def dodaj_pare(slovar, pari):
    for k, v in pari:
        slovar[k] = v

def nakljucen_dict(n):
    d = {}
    dodaj_pare(d, nakljucni_pari(n))
    return d

def nakljucen_slovar(n):
    d = Slovar()
    dodaj_pare(d, nakljucni_pari(n))
    return d

stopaj.izmeri_case_poskusov(
    [nakljucen_dict(2**n) for n in range(10, 20)],
    [
        lambda slovar: poisci(slovar, 0),
    ],
)

stopaj.izmeri_case_poskusov(
    [nakljucen_slovar(2**n) for n in range(10, 20)],
    [
        lambda slovar: poisci(slovar, 0),
    ],
)
