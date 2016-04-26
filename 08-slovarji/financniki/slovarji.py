nujne_telefonske_stevilke = {
    'policija': 113,
    'gasilci': 112,
    'točen čas': 195
}

rimske_stevilke = {
    1: 'I',
    2: 'II',
    3: 'III',
    4: 'IV'
}

def prestej_crke(niz):
    '''Vrne slovar pojavitev črk v danem nizu.'''
    pojavitve = {}
    for znak in niz:
        if znak in pojavitve:
            pojavitve[znak] += 1
        else:
            pojavitve[znak] = 1
    return pojavitve


def prestej_crke(niz):
    '''Vrne slovar pojavitev črk v danem nizu.'''
    pojavitve = {}
    for znak in niz:
        pojavitve[znak] = pojavitve.get(znak, 0) + 1
    return pojavitve

prestej_crke("abrakadabra")


def pridna(x):
    y = 2 * x
    return y

def poredna(x):
    y = 2 * x
    print(y)

tviter = {
    'Ana': {'Bojan', 'David', 'Eva'},
    'Bojan': {},
    'Cene': {'Ana', 'David'},
    'David': {'David'},
    'Eva': {'Ana', 'Bojan'}
}


def prestej_sledilce(sledilci):
    '''Vrne slovar, v katerem za vsako osebo piše število njenih sledilcev.'''
    stevilo_sledilcev = {}
    for oseba in sledilci:
        stevilo_sledilcev[oseba] = len(sledilci[oseba])
    return stevilo_sledilcev


def najbolj_popularen(sledilci):
    '''Vrne ime osebe z največ sledilci.'''
    najbolj_popularna_do_zdaj = None

    for oseba in sledilci:
        if najbolj_popularna_do_zdaj is None or len(sledilci[oseba]) > len(sledilci[najbolj_popularna_do_zdaj]):
            najbolj_popularna_do_zdaj = oseba

    return najbolj_popularna_do_zdaj


def poisci_sledene(sledilci):
    sledeni = {}
    for sledena_oseba, sledilci_osebe in sledilci.items():
        for sledilec in sledilci_osebe:
            if sledilec in sledeni:
                sledeni[sledilec].add(sledena_oseba)
            else:
                sledeni[sledilec] = {sledena_oseba}
    return sledeni
