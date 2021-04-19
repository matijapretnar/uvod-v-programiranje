from model import Model, Spisek, Opravilo

moj_model = Model()

DODAJ_SPISEK = 1
POBRISI_SPISEK = 2
ZAMENJAJ_SPISEK = 3
DODAJ_OPRAVILO = 4
POBRISI_OPRAVILO = 5
OPRAVI_OPRAVILO = 6
IZHOD = 7


def preberi_stevilo():
    while True:
        vnos = input('> ')
        try:
            return int(vnos)
        except ValueError:
            print('Vnesti morate število.')

def izberi_moznost(moznosti):
    '''Uporabniku našteje možnosti ter vrne izbrano.'''
    for i, (_moznost, opis) in enumerate(moznosti, 1):
        print(f'{i}) {opis}')
    while True:
        i = preberi_stevilo()
        if 1 <= i <= len(moznosti):
            moznost, _opis = moznosti[i - 1]
            return moznost
        else:
            print(f'Vnesti morate število med 1 in {len(moznosti)}.')

def prikaz_spiska(spisek):
    vsa = spisek.stevilo_vseh()
    zamujena = spisek.stevilo_zamujenih()
    if zamujena:
        return f'{spisek.ime} ({zamujena}!!! + {vsa - zamujena})'
    else:
        return f'{spisek.ime} ({vsa})'

# faks (3!!! + 2)
# doma (10)

def prikaz_opravila(opravilo):
    if opravilo.zamuja():
        return f'!!!{opravilo.ime}'
    elif opravilo.rok:
        return f'{opravilo.ime} ({opravilo.rok})'
    else:
        return f'{opravilo.ime}'

def izberi_spisek(model):
    return izberi_moznost([(spisek, prikaz_spiska(spisek)) for spisek in model.spiski])

def izberi_opravilo(model):
    return izberi_moznost([(opravilo, prikaz_opravila(opravilo)) for opravilo in model.aktualni_spisek.opravila])

def tekstovni_vmesnik():
    prikazi_pozdravno_sporocilo()
    while True:
        prikazi_aktualna_opravila()
        ukaz = izberi_moznost([
            (DODAJ_SPISEK, "dodaj nov spisek"),
            (POBRISI_SPISEK, "pobriši spisek"),
            (ZAMENJAJ_SPISEK, "prikaži drug spisek"),
            (DODAJ_OPRAVILO, "dodaj novo opravilo"),
            (POBRISI_OPRAVILO, "pobriši opravilo"),
            (OPRAVI_OPRAVILO, "opravi opravilo"),
            (IZHOD, "zapri program"),
        ])
        if ukaz == DODAJ_SPISEK:
            dodaj_spisek()
        elif ukaz == POBRISI_SPISEK:
            pobrisi_spisek()
        elif ukaz == ZAMENJAJ_SPISEK:
            zamenjaj_spisek()
        elif ukaz == DODAJ_OPRAVILO:
            dodaj_opravilo()
        elif ukaz == POBRISI_OPRAVILO:
            pobrisi_opravilo()
        elif ukaz == OPRAVI_OPRAVILO:
            opravi_opravilo()
        elif ukaz == IZHOD:
            print('Nasvidenje!')
            break

def prikazi_pozdravno_sporocilo():
    print('Pozdravljeni!')

def prikazi_aktualna_opravila():
    if moj_model.aktualni_spisek:
        for opravilo in moj_model.aktualni_spisek.opravila:
            if not opravilo.opravljeno:
                print(f'- {prikaz_opravila(opravilo)}')
    else:
        print('Ker nimate še nobenega spiska, morate enega ustvariti.')
        dodaj_spisek()

def dodaj_spisek():
    print('Vnesite podatke novega spiska.')
    ime = input('Ime> ')
    nov_spisek = Spisek(ime)
    moj_model.dodaj_spisek(nov_spisek)

def pobrisi_spisek():
    spisek = izberi_spisek(moj_model)
    moj_model.pobrisi_spisek(spisek)

def zamenjaj_spisek():
    print('Izberite spisek, na katerega bi preklopili.')
    spisek = izberi_spisek(moj_model)
    moj_model.zamenjaj_spisek(spisek)

def dodaj_opravilo():
    print('Vnesite podatke novega opravila.')
    ime = input('Ime> ')
    opis = input('Opis> ')
    rok = None
    novo_opravilo = Opravilo(ime, opis, rok)
    moj_model.dodaj_opravilo(novo_opravilo)

def pobrisi_opravilo():
    opravilo = izberi_opravilo(moj_model)
    moj_model.pobrisi_opravilo(opravilo)

def opravi_opravilo():
    opravilo = izberi_opravilo(moj_model)
    opravilo.opravi()

tekstovni_vmesnik()