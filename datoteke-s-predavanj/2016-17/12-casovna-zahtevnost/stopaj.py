import matplotlib.pyplot as plt
import random
import timeit

 
def najvecji_element1(sez):
    maksi = None
    for x in sez:
        if maksi is None or x > maksi:
            maksi = x
    return maksi

def najvecji_element2(sez):
    for x in sez:
        if x == max(sez):
            return x

def dodaj_na_konec_seznama(sez, x=0):
    sez.append(x)

def dodaj_na_zacetek_seznama(sez, x=0):
    sez.insert(0, x)

def isci(elementi, x=-1):
    return x in elementi

def nakljucen_seznam(dolzina):
    seznam = []
    for _ in range(dolzina):
        seznam.append(random.random())
    return seznam

def izmeri_case_poskusov(vzorci, funkcije, velikost=len, stevilo_poskusov=10):
    if not isinstance(funkcije, list):
        funkcije = [funkcije]

    velikosti = []
    grafi = []
    vsi_casi = []
    for x in vzorci:
        velikosti.append(velikost(x))
    for i, f in enumerate(funkcije):
        casi = []
        for x in vzorci:
            cas = timeit.timeit('f(x)', number=stevilo_poskusov, globals=locals())
            vsi_casi.append(cas)
            casi.append(cas)
        grafi.append(plt.scatter(velikosti, casi))
    plt.ylim([0, sorted(vsi_casi)[int(0.98 * len(vsi_casi))]])
    plt.legend(grafi, [f.__name__ for f in funkcije])
    plt.show()

seznami = [list(range(n)) for n in range(1, 100, 1)]
mnozice = [set(range(n)) for n in range(1, 10000, 100)]

izmeri_case_poskusov(seznami, [najvecji_element1, najvecji_element2])
izmeri_case_poskusov(seznami, [dodaj_na_zacetek_seznama, dodaj_na_konec_seznama])
izmeri_case_poskusov(seznami, isci)
izmeri_case_poskusov(mnozice, isci)
izmeri_case_poskusov(mnozice, sum)
izmeri_case_poskusov(seznami, sum)
