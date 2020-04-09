ze_izracunane_vrednosti = {}

def g(x):
    if x not in ze_izracunane_vrednosti:
        print(f'Računam g({x})')
        y = 10 + x
        print(f'...še kar računam...')
        z = y - x
        print(f'g({x}) = {z}')
        ze_izracunane_vrednosti[x] = z
    return ze_izracunane_vrednosti[x]

def funkcija_ki_vzame_funkcijo_in_izracuna_njeno_vrednost_na_nic(f):
    return f(0)

def povprecje_kvadratov(sez):
    vsota = 0
    for x in sez:
        vsota += x ** 2
    return vsota / len(sez)

import math

def povprecje_sinusov(sez):
    vsota = 0
    for x in sez:
        vsota += math.sin(x)
    return vsota / len(sez)

def povprecje_funkcije(f, sez):
    vsota = 0
    for x in sez:
        vsota += f(x)
    return vsota / len(sez)

def funkcija_ki_poveca_za(a):
    def funki(x):
        return x + a
    return funki

def naredi_pametno_funkcijo_ki_si_zapomni_rezultate(neumni_f):

    ze_izracunane_vrednosti_za_f = {}

    def pametni_f(x):
        if x not in ze_izracunane_vrednosti_za_f:
            y = neumni_f(x)
            ze_izracunane_vrednosti_za_f[x] = y
        return ze_izracunane_vrednosti_za_f[x]

    return pametni_f

@naredi_pametno_funkcijo_ki_si_zapomni_rezultate
def f(x):
    print(f'Računam f({x})')
    y = 10 * x
    print(f'f({x}) = {y}')
    return y