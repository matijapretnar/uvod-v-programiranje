import stopaj


def poisci1(sez, x):        # seznam velikosti n
                            # celotna funkcija: O(n) + O(1) = O(n)
                            # zanka ... O(n) * O(1) = O(n)
    for y in sez:           # obhodov: največ n ... O(n)
        if y == x:          # O(1)
            return True     # O(1)
    return False            # O(1)


def poisci2(sez, x):
    return x in sez # O(n)


def poisci_v_urejenem(sez, x, i=0, j=None):
    if j is None:
        j = len(sez)
    if i >= j:
        return False
    else:
        sredina = (i + j) // 2
        if x == sez[sredina]:
            return True
        elif x < sez[sredina]:
            return poisci_v_urejenem(sez, x, i, sredina)
        elif x > sez[sredina]:
            return poisci_v_urejenem(sez, x, sredina + 1, j)
        else:
            assert False

def poisci_v_urejenem_brez_potratne_rekurzije(sez, x):
    i = 0
    j = len(sez)
    while i < j:
        sredina = (i + j) // 2
        if x == sez[sredina]:
            return True
        elif x < sez[sredina]:
            j = sredina
        elif x > sez[sredina]:
            i = sredina + 1
        else:
            assert False
    return False

stopaj.izmeri_case_poskusov(
    [stopaj.nakljucen_narascajoc_seznam(5000 * n) for n in range(1, 20)],
    [
        lambda sez: poisci1(sez, sez[-1]),
        lambda sez: poisci2(sez, sez[-1]),
        lambda sez: poisci_v_urejenem(sez, sez[-1], 0),
        lambda sez: poisci_v_urejenem_brez_potratne_rekurzije(sez, sez[-1]),
    ],
)
