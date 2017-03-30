import os

def poisci_datoteke(mapa, koncnice=['.avi', '.mp4', '.mkv']):
    datoteke = []

    for pot in os.listdir(mapa):
        pot = os.path.join(mapa, pot)
        if os.path.isdir(pot):
            datoteke += poisci_datoteke(pot, koncnice=koncnice)
        else:
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


def cisto_ime(serija, sezona, epizoda, koncnica):
    mapa_serije = serija
    mapa_sezone = 'Sezona {}'.format(sezona)
    ime_datoteke = '{} S{:02}E{:02}{}'.format(serija, sezona, epizoda, koncnica)
    return os.path.join(mapa_serije, mapa_sezone, ime_datoteke)


def pocisti(mapa, serija):
    for stara_pot in poisci_datoteke(mapa):
        _, datoteka = os.path.split(stara_pot)
        stevilke = izloci_stevilke(datoteka)
        _, koncnica = os.path.splitext(datoteka)
        nova_pot = cisto_ime(serija, stevilke[0], stevilke[1], koncnica)
        print("{} --> {}".format(stara_pot, nova_pot))
        vsota = 0
        for i in range(3000000):
            vsota += i
        nova_mapa, _ = os.path.split(nova_pot)
        os.makedirs(nova_mapa, exist_ok=True)
        os.rename(stara_pot, nova_pot)



# pocisti('igra', 'Igra prestolov')
