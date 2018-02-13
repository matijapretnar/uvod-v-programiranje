import matplotlib.pyplot as plt
import random
import timeit

 
def najvecji_element1(sez):           # O(1) + O(n) + O(1) = O(n)
    maksi = None                        # O(1)
    for x in sez:                       # n * O(1) = O(n)
        if maksi is None or x > maksi:    # O(1)
            maksi = x                       # O(1)
    return maksi                        # O(1)

def najvecji_element2(sez):
    for x in sez:                     # n * O(n) = O(n^2)
        if x == max(sez):               # O(n)
            return x                      # O(1)

def pametna_sled(mat):
    sled = 0
    for i in range(len(mat)):
        sled += mat[i][i]
    return sled

def neumna_sled(mat):
    sled = 0
    for i in range(len(mat)):
        for j in range(len(mat)):
            if i == j:
                sled += mat[i][j]
    return sled

def dodaj_na_konec_seznama(sez, x=0):
    sez.append(x)

def dodaj_na_zacetek_seznama(sez, x=0):
    sez.insert(0, x)

def spremeni_seznam(sez):
    sez[0] = 0
    sez[-1] = 0

def isci_na_roke(elementi, x=-1):
    for y in elementi:
        if x == y:
            return True
    return False

def isci_python(elementi, x=-1):
    return x in elementi

def isci_v_urejenem_seznamu(elementi, x=-1, od=0, do=None):
    if do is None:
        do = len(elementi)
    sredina = (od + do) // 2
    if x == elementi[sredina]:
        return True
    elif od == do - 1:
        return False
    elif x < elementi[sredina]:
        return isci_v_urejenem_seznamu(elementi, x, od, sredina)
    elif x > elementi[sredina]:
        return isci_v_urejenem_seznamu(elementi, x, sredina + 1, do)

print(isci_v_urejenem_seznamu([0, 1, 2, 5, 8, 10, 20, 40, 60], 3, 0, 9))

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

print(nakljucna_matrika(3))

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

seznami = [list(range(n)) for n in range(1, 100000, 1000)]
mnozice = [set(range(n)) for n in range(1, 100000, 1000)]
matrike = [nakljucna_matrika(n) for n in range(1, 40)]

# izmeri_case_poskusov(matrike, [neumna_sled, pametna_sled])
# izmeri_case_poskusov(seznami, [najvecji_element1, najvecji_element2, max])
# izmeri_case_poskusov(seznami, [dodaj_na_zacetek_seznama, dodaj_na_konec_seznama])
# izmeri_case_poskusov(seznami, [spremeni_seznam])
izmeri_case_poskusov(mnozice, isci_python)
# izmeri_case_poskusov(mnozice, sum)
# izmeri_case_poskusov(seznami, sum)
