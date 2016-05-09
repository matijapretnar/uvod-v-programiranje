import os


def naberi_datoteke(imenik, koncnice=['.avi', '.mkv', '.mp4']):
    '''Vrne seznam polnih poti vseh datotek v imeniku z danimi končnicami.'''
    datoteke = []
    for datoteka in os.listdir(imenik):
        pot = os.path.join(imenik, datoteka)
        if os.path.isdir(pot):
            datoteke += naberi_datoteke(pot)
        elif os.path.isfile(pot):
            _, koncnica = os.path.splitext(pot)
            if koncnica in koncnice:
                datoteke.append(pot)
    return datoteke


def izloci_stevilke(niz):
    '''Vrne seznam vseh naravnih števil, ki se pojavljajo v nizu.'''
    stevilke = []
    stevilka = None
    for znak in niz:
        if znak.isdigit():
            if stevilka is None:
                stevilka = int(znak)
            else:
                stevilka = 10 * stevilka + int(znak)
        else:
            if stevilka is not None:
                stevilke.append(stevilka)
                stevilka = None
    if stevilka is not None:
        stevilke.append(stevilka)
    return stevilke


def sezona_epizoda(datoteka):
    _, ime = os.path.split(datoteka)
    stevilke = izloci_stevilke(ime)
    return stevilke[0], stevilke[1]


def koncni_cilj(ime_serije, sezona, epizoda, koncnica):
    '''Vrne prečiščeno pot za dano datoteko.'''
    mapa = 'Sezona {}'.format(sezona)
    datoteka = '{} S{:02}E{:02}{}'.format(ime_serije, sezona, epizoda, koncnica)
    return os.path.join(ime_serije, mapa, datoteka)


def uredi(neurejena_mapa, ime_serije):
    datoteke = naberi_datoteke(neurejena_mapa)
    for datoteka in datoteke:
        _, koncnica = os.path.splitext(datoteka)
        sezona, epizoda = sezona_epizoda(datoteka)
        nova_pot = koncni_cilj(ime_serije, sezona, epizoda, koncnica)
        nova_mapa, _ = os.path.split(nova_pot)
        os.makedirs(nova_mapa, exist_ok=True)
        os.rename(datoteka, nova_pot)


uredi('igra', 'Game of Thrones')
