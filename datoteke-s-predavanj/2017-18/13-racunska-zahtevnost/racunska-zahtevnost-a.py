import stopaj


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


def najvecji_element3(sez):
    maksi = max(sez)
    for x in sez:
        if x == maksi:
            return x


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


def isci(seznam, x):
    if len(seznam) == 0:
        return False
    else:
        indeks_sredine = len(seznam) // 2
        sredina = seznam[indeks_sredine]
        if x == sredina:
            return True
        elif x < sredina:
            return isci(seznam[:indeks_sredine], x)
        else:  # x > sredina
            return isci(seznam[indeks_sredine + 1:], x)


def isci_dolzino(seznam):
    return isci(seznam, len(seznam))


stopaj.izmeri_case_poskusov(
    [stopaj.nakljucen_narascajoc_seznam(10000 * n) for n in range(20)],
    [isci_dolzino]
)
