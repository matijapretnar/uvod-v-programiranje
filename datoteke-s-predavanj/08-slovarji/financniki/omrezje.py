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
    for oseba, sledeni in omrezje.items():
        stevilo[oseba] = len(sledeni)
    return stevilo


def stevilo_sledenih_izpeljani(omrezje):
    '''Vrne slovar, v katerem vsaki osebi pripada število sledenih oseb.'''
    return {oseba: len(sledeni) for oseba, sledeni in omrezje.items()}


def stevilo_sledilcev(omrezje):
    '''Vrne slovar, v katerem vsaki osebi pripada število sledilcev.'''
    kolikokrat_se_pojavi = {}
    for mnozica in omrezje.values():
        for oseba in mnozica:
            if oseba in kolikokrat_se_pojavi:
                kolikokrat_se_pojavi[oseba] += 1
            else:
                kolikokrat_se_pojavi[oseba] = 1
    return kolikokrat_se_pojavi


def najpopularnejsa_oseba(omrezje):
    '''Vrne osebo z največ sledilci.'''
    sledilci = stevilo_sledilcev(omrezje)
    najbolj_popularna = None
    for oseba, st_sledilcev in sledilci.items():
        if najbolj_popularna is None or st_sledilcev > sledilci[najbolj_popularna]:
            najbolj_popularna = oseba
    return najbolj_popularna


def poisci_sledilce(omrezje):
    '''Vrne slovar, v katerem vsaki osebi pripada množica vseh, ki ji sledijo.'''
    ...


def priporoci_nove(omrezje, oseba):
    '''Za dano osebo vrne množico priporočil, komu naj še sledi.

    Priporočila se izračunajo tako, da se vzame vse osebe, ki ji sledijo
    sledene osebe, vendar še niso med sledenimi.'''
    priporocila = set()
    for ze_sledena_oseba in omrezje[oseba]:
        for nova_oseba in omrezje[ze_sledena_oseba]:
            if nova_oseba not in omrezje[oseba] and nova_oseba != oseba:
                priporocila.add(nova_oseba)
    return priporocila



def priporoci_nove(omrezje, oseba):
    '''Za dano osebo vrne množico priporočil, komu naj še sledi.

    Priporočila se izračunajo tako, da se vzame vse osebe, ki ji sledijo
    sledene osebe, vendar še niso med sledenimi.'''
    priporocila = set()
    for ze_sledena_oseba in omrezje[oseba]:
        priporocila |= omrezje[ze_sledena_oseba]
    return priporocila - omrezje[oseba] - {oseba}
