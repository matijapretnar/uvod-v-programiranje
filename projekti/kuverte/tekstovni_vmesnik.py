from model import Proracun, Kuverta, Racun, Preliv
from datetime import date

proracun = Proracun()
hrana = Kuverta('hrana')
racuni = Kuverta('računi')
zabava = Kuverta('zabava')
gotovina = Racun('gotovina')
tekoci_racun = Racun('tekoči račun')
proracun.dodaj_kuverto(hrana)
proracun.dodaj_kuverto(racuni)
proracun.dodaj_kuverto(zabava)
proracun.dodaj_racun(gotovina)
proracun.dodaj_racun(tekoci_racun)
zadnji_nakup = Preliv(15, 'špageti in pivo', date(2021, 4, 12), gotovina, hrana)
gotovina.dodaj_preliv(zadnji_nakup)
hrana.dodaj_preliv(zadnji_nakup)

###########################################################
# Pomožne funkcije za prikaz
###########################################################

def krepko(niz):
    return f'\033[1m{niz}\033[0m'

def dobro(niz):
    return f'\033[1;94m{niz}\033[0m'

def slabo(niz):
    return f'\033[1;91m{niz}\033[0m'

def prikaz_zneska(ime, stanje):
    if stanje > 0:
        return f'{ime}: {dobro(stanje)} €'
    elif stanje < 0:
        return f'{ime}: {slabo(stanje)} €'
    else:
        return f'{ime}: 0 €'

def prikaz_racuna(racun):
    return prikaz_zneska(racun.ime, racun.stanje())

def prikaz_kuverte(kuverta):
    if kuverta is None:
        return prikaz_zneska('nerazporejeno', proracun.nerazporejena_sredstva())
    else:
        return prikaz_zneska(kuverta.ime, kuverta.stanje())

###########################################################
# Pomožne funkcije za vnos
###########################################################

def vnesi_stevilo(pozdrav):
    """S standardnega vhoda prebere naravno število."""
    while True:
        try:
            stevilo = input(pozdrav)
            return int(stevilo)
        except ValueError:
            print(slabo('Prosim, da vnesete število!'))


def izberi(seznam):
    """
    Uporabniku omogoči interaktivno izbiro elementa iz seznama.
    
    Funkcija sprejme seznam parov (oznaka, element), prikaže seznam
    oznak ter vrne element, ki ustreza vpisani oznaki.
    >>> izberi([('deset', 10), ('trideset', 30)])
    1) deset
    2) trideset
    > 2
    30
    """
    for indeks, (oznaka, _) in enumerate(seznam, 1):
        print(f'{indeks}) {oznaka}')
    while True:
        izbira = vnesi_stevilo('> ')
        if 1 <= izbira <= len(seznam):
            _, element = seznam[izbira - 1]
            return element
        else:
            print(slabo(f'Izberi število med 1 in {len(seznam)}'))


def izberi_kuverto(kuverte):
    return izberi([(prikaz_kuverte(kuverta), kuverta) for kuverta in kuverte])

def izberi_racun(racuni):
    return izberi([(prikaz_racuna(racun), racun) for racun in racuni])

###########################################################
# Tekstovni vmesnik
###########################################################

def tekstovni_vmesnik():
    uvodni_pozdrav()
    while True:
        osnovni_zaslon()

def uvodni_pozdrav():
    print('Pozdravljen!')

def osnovni_zaslon():
    print('Kaj bi rad počel?')
    print('1) pogledal kuverte')
    print('2) pogledal račune')
    vnos = input('> ')
    if vnos == '1':
        pokazi_kuverte()
    elif vnos == '2':
        pokazi_racune()

def pokazi_kuverte():
    for kuverta in proracun.kuverte:
        print(f'- {kuverta.ime}: {kuverta.stanje()}')


tekstovni_vmesnik()