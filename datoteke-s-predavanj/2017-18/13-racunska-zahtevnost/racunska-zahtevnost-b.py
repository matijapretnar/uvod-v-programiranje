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

def najvecji_element4(sez):
    maksi = max(sez)
    return maksi

najvecji_element5 = max

def isci(seznam, x, od=0, do=None):
    '''Poisci, ali x nastopa v rezini seznam[od:do]'''
    if do is None:
        do = len(seznam)
    if do <= od:
        return False
    else:
        indeks_sredine = (od + do) // 2
        sredina = seznam[indeks_sredine]
        if x == sredina:
            return True
        elif x < sredina:
            return isci(seznam, x, od, indeks_sredine)
        else:  # x > sredina
            return isci(seznam, x, indeks_sredine + 1, do)


def isci_dolzino(seznam):
    return isci(seznam, -42)


stopaj.izmeri_case_poskusov(
    [stopaj.narascajoc_seznam(10000 * n + 1) for n in range(100)],
    [
        isci_dolzino,
    ]
)
