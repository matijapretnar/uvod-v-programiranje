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

def izmeri_case_poskusov(vzorci, f, velikost=len, stevilo_poskusov=10):
    velikosti, casi = [], []
    for x in vzorci:
        velikosti.append(velikost(x))
        cas = timeit.timeit('f(x)', number=stevilo_poskusov, globals=locals())
        casi.append(cas)
    plt.scatter(velikosti, casi)
    plt.ylim([0, max(casi)])
    plt.title(f.__name__)
    plt.show()

def nakljucen_seznam(dolzina):
    seznam = []
    for _ in range(dolzina):
        seznam.append(random.random())
    return seznam

seznami = [list(range(n)) for n in range(1, 10000, 100)]
mnozice = [set(range(n)) for n in range(1, 10000, 100)]

izmeri_case_poskusov(seznami, dodaj_na_zacetek_seznama)
izmeri_case_poskusov(seznami, dodaj_na_konec_seznama)
izmeri_case_poskusov(seznami, isci)
izmeri_case_poskusov(mnozice, isci)
izmeri_case_poskusov(mnozice, sum)
izmeri_case_poskusov(seznami, sum)
