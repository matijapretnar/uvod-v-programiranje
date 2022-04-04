import matplotlib.pyplot as plt
import random
import timeit


def narascajoc_seznam(dolzina):
    return list(range(dolzina))


def padajoc_seznam(dolzina):
    return list(range(dolzina)[::-1])


def nakljucen_seznam(dolzina):
    seznam = []
    for _ in range(dolzina):
        seznam.append(random.randint(0, 10 * dolzina))
    return seznam


def nakljucen_narascajoc_seznam(dolzina):
    return sorted(nakljucen_seznam(dolzina))


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

    velikosti = [velikost(x) for x in vzorci]
    grafi = []
    vsi_casi = []
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
