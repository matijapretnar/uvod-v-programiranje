from datetime import date
from model import Proracun

proracun = Proracun()

# Polnjenje začetnega proračuna s testnimi podatki (bo šlo ven)

gotovina = proracun.nov_racun('gotovina')
tekoci_racun = proracun.nov_racun('tekoči račun')
vreca = proracun.nova_kuverta('💰')

proracun.nov_preliv(230, date(2020, 4, 1), 'štipendija', tekoci_racun, None)
proracun.nov_preliv(-30, date(2020, 4, 3), 'prevoz', tekoci_racun, vreca)
proracun.nov_preliv(-40, date(2020, 4, 5), 'hlače', gotovina, vreca)
proracun.nov_preliv(150, date(2020, 4, 20), 'krizni dodatek', tekoci_racun, None)
proracun.nov_preliv(-150, date(2020, 4, 20), 'hlače', tekoci_racun, vreca)
proracun.nov_preliv(-100, date(2020, 4, 30), 'najemnina', tekoci_racun, vreca)
proracun.nov_preliv(-10, date(2020, 4, 30), 'telefon', tekoci_racun, vreca)
proracun.nov_preliv(-40, date(2020, 5, 4), 'hrana', gotovina, vreca)

# Pomožne funkcije za vnos

def napaka(niz):
    print('\033[1;91m' + niz + '\033[0m')


def uspeh(niz):
    print('\033[1;94m' + niz + '\033[0m')


def vnesi_stevilo(pozdrav):
    """S standardnega vhoda prebere naravno število."""
    while True:
        try:
            stevilo = input(pozdrav)
            return int(stevilo)
        except ValueError:
            napaka(f'Prosim, da vnesete število!')


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
            napaka(f'Izberi število med 1 in {len(seznam)}')

# Sestavni deli uporabniškega vmesnika

LOGO = '''
______                     ___                                 _ _       
| ___ \                    \_/                                | (_)      
| |_/ / __ ___  _ __ __ _  ___ _   _ _ __   _____   _____   __| |_  __ _ 
|  __/ '__/ _ \| '__/ _` |/ __| | | | '_ \ / _ \ \ / / _ \ / _` | |/ _` |
| |  | | | (_) | | | (_| | (__| |_| | | | | (_) \ V / (_) | (_| | | (_| |
\_|  |_|  \___/|_|  \__,_|\___|\__,_|_| |_|\___/ \_/ \___/ \__,_| |\__,_|
                                                               _/ |      
                                                              |__/
'''


def glavni_meni():
    print(LOGO)
    print('Pozdravljeni v programu računovodja!')
    print('Za izhod pritisnite Ctrl-C.')
    while True:
        try:
            print()
            print('Kaj bi radi naredili?')
            moznosti = [
                ('vnesel priliv/odliv', dodaj_preliv),
                ('dodal nov račun', dodaj_racun),
                ('dodal novo kuverto', dodaj_kuverto),
                ('pogledal stanje', poglej_stanje),
            ]
            izbira = izberi(moznosti)
            izbira()
        except ValueError as e:
            napaka(e.args[0])
        except KeyboardInterrupt:
            print()
            print('Nasvidenje!')
            return


def dodaj_preliv():
    znesek = vnesi_stevilo('Znesek> ')
    datum = date.today()
    opis = input('Opis> ')
    print('Račun:')
    racun = izberi([(racun.ime, racun) for racun in proracun.racuni])
    print('Kuverta:')
    kuverta = izberi([(kuverta.ime, kuverta) for kuverta in proracun.kuverte])
    proracun.nov_preliv(znesek, datum, opis, racun, kuverta)
    uspeh('Preliv uspešno dodan!')


def dodaj_racun():
    ime_racuna = input('Vnesi ime računa> ')
    proracun.nov_racun(ime_racuna)
    uspeh('Račun uspešno dodan!')


def dodaj_kuverto():
    ime_kuverte = input('Vnesi ime kuverte> ')
    proracun.nova_kuverta(ime_kuverte)
    uspeh('Kuverta uspešno dodana!')


def poglej_stanje():
    print('RAČUNI:')
    for racun in proracun.racuni:
        print(racun)
    print('KUVERTE:')
    for kuverta in proracun.kuverte:
        print(kuverta)
    print('NERAZPOREJENO:')
    print(proracun.nerazporejena_sredstva())


glavni_meni()
