import os


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

def relevantne_datoteke(imenik, koncnice={'.mp4', '.mkv', '.avi'}):
    for delna_pot in os.listdir(imenik):
        cela_pot = os.path.join(imenik, delna_pot)
        if os.path.isdir(cela_pot):
            yield from relevantne_datoteke(cela_pot, koncnice=koncnice)
        else:
            _, koncnica = os.path.splitext(cela_pot)
            if koncnica in koncnice:
                yield cela_pot


def polepsaj_ime_datoteke(cela_pot):
    _, ime_datoteke = os.path.split(cela_pot)
    ime, koncnica = os.path.splitext(ime_datoteke)
    sezona, epizoda, *ostale = izloci_stevilke(ime)
    return 'Igra prestolov S{0:02}E{1:02}{2}'.format(sezona, epizoda, koncnica)


def preimenuj(grdo_ime):
    lepo_ime = polepsaj_ime_datoteke(grdo_ime)
    print(grdo_ime, '~~>', lepo_ime)
    # os.rename(grdo_ime, lepo_ime)

for pot in relevantne_datoteke('igra'):
    preimenuj(pot)
