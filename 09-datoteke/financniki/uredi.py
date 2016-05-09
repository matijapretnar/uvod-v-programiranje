import os


def poisci_datoteke(mapa, koncnice=['.mkv', '.avi', '.mp4']):
    datoteke = []
    for datoteka in os.listdir(mapa):
        polna_pot = os.path.join(mapa, datoteka)
        if os.path.isdir(polna_pot):
            datoteke += poisci_datoteke(polna_pot, koncnice=koncnice)
        else:
            _, koncnica = os.path.splitext(polna_pot)
            if koncnica in koncnice:
                datoteke.append(polna_pot)
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


def novo_ime(ime_serije, pot_do_datoteke):
    _, ime_datoteke = os.path.split(pot_do_datoteke)
    stevilke_v_imenu = izloci_stevilke(ime_datoteke)
    sezona, epizoda = stevilke_v_imenu[0], stevilke_v_imenu[1]
    _, koncnica = os.path.splitext(ime_datoteke)
    novo_ime = '{0} S{1:02}E{2:02}{3}'.format(ime_serije, sezona, epizoda, koncnica)
    return os.path.join(ime_serije, 'Sezona {}'.format(sezona), novo_ime)


def uredi(neurejena_mapa, ime_serije):
    for stara_datoteka in poisci_datoteke(neurejena_mapa):
        nova_datoteka = novo_ime(ime_serije, stara_datoteka)
        nova_mapa, _ = os.path.split(nova_datoteka)
        os.makedirs(nova_mapa, exist_ok=True)
        os.rename(stara_datoteka, nova_datoteka)
