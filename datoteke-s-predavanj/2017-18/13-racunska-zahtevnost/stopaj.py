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

################################################################################


def nakljucen_seznam(dolzina):
    seznam = []
    for _ in range(dolzina):
        seznam.append(random.random())
    return seznam


def nakljucna_matrika(n):
    matrika = []
    for _ in range(n):
        vrstica = []
        for _ in range(n):
            vrstica.append(random.random())
        matrika.append(vrstica)
    return matrika


def izmeri_case_poskusov(vzorci, funkcije, velikost=len, stevilo_poskusov=10):
    if not isinstance(funkcije, list):
        funkcije = [funkcije]

    velikosti = []
    grafi = []
    vsi_casi = []
    for x in vzorci:
        velikosti.append(velikost(x))
    for i, f in enumerate(funkcije):
        print(f.__name__, end='', flush=True)
        casi = []
        for x in vzorci:
            cas = timeit.timeit('f(x)', number=stevilo_poskusov, globals=locals())
            vsi_casi.append(cas)
            casi.append(cas)
            print('.', end='', flush=True)
        print()
        grafi.append(plt.scatter(velikosti, casi))
    plt.ylim([0, sorted(vsi_casi)[int(0.98 * len(vsi_casi))]])
    plt.legend(grafi, [f.__name__ for f in funkcije])
    plt.show()


seznami = [list(range(n)) for n in range(1, 1000, 10)]


izmeri_case_poskusov(seznami, [najvecji_element1, najvecji_element2, max])
