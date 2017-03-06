tviter = {
    'Ana': {'Bojan', 'David', 'Eva'},
    'Bojan': set(),
    'Cene': {'Ana', 'David'},
    'David': {'David'},
    'Eva': {'Ana', 'Bojan'}
}


def stevilo_sledenih(omrezje):
    '''Vrne slovar, v katerem vsaki osebi pripada število sledenih oseb.'''
    stevilo = {}
    for oseba in omrezje:
        stevilo[oseba] = len(omrezje[oseba])
    return stevilo



def stevilo_sledenih(omrezje):
    '''Vrne slovar, v katerem vsaki osebi pripada število sledenih oseb.'''
    return {oseba: len(omrezje[oseba]) for oseba in omrezje}





def najpopularnejsa_oseba(omrezje):
    '''Vrne osebo z največ sledilci.'''
    stevilo_sledilcev = {}
    for mnozica_sledenih in omrezje.values():
        for sledeni in mnozica_sledenih:
            stevilo_sledilcev[sledeni] = stevilo_sledilcev.get(sledeni, 0) + 1

    if stevilo_sledilcev:
        return poisci_kljuc(stevilo_sledilcev, max(stevilo_sledilcev.values()))
    else:
        return None


def poisci_kljuc(slovar, pripadajoca_vrednost):
    for kljuc in slovar:
        if slovar[kljuc] == pripadajoca_vrednost:
            return kljuc
    return None


def poisci_sledilce(omrezje):
    '''Vrne slovar, v katerem vsaki osebi pripada množica vseh, ki ji sledijo.'''
    ...


def priporoci_nove(omrezje):
    '''Vrne slovar, kjer vsaki osebi pripadajo priporočila, komu naj še sledi.

    Priporočila se izračunajo tako, da se vzame vse osebe, ki ji sledijo
    sledene osebe, vendar še niso med sledenimi.'''
    ...
