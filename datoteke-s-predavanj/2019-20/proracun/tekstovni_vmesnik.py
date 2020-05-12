from datetime import date
from model import Proracun

proracun = Proracun()

gotovina = proracun.dodaj_racun('gotovina')
tekoci_racun = proracun.dodaj_racun('tekoči račun')
vreca = proracun.dodaj_kuverto('💰')

proracun.dodaj_preliv(230, date(2020, 4, 1), 'štipendija', tekoci_racun, vreca)
proracun.dodaj_preliv(-30, date(2020, 4, 3), 'prevoz', tekoci_racun, vreca)
proracun.dodaj_preliv(-40, date(2020, 4, 5), 'hlače', gotovina, vreca)
proracun.dodaj_preliv(150, date(2020, 4, 20), 'krizni dodatek', tekoci_racun, vreca)
proracun.dodaj_preliv(-150, date(2020, 4, 20), 'hlače', tekoci_racun, vreca)
proracun.dodaj_preliv(-100, date(2020, 4, 30), 'najemnina', tekoci_racun, vreca)
proracun.dodaj_preliv(-10, date(2020, 4, 30), 'telefon', tekoci_racun, vreca)
proracun.dodaj_preliv(-40, date(2020, 5, 4), 'hrana', gotovina, vreca)

def vnesi_stevilo(pozdrav):
    while True:
        stevilo = input(pozdrav)
        if stevilo.isdigit():
            return int(stevilo)
        else:
            print(f'Prosim, da vneseš število!')


def izberi(seznam):
    for indeks, element in enumerate(seznam, 1):
        print(f'{indeks}) {element}')
    while True:
        izbira = vnesi_stevilo('> ')
        if 1 <= izbira <= len(seznam):
            return seznam[izbira - 1]
        else:
            print(f'Izberi število med 1 in {len(seznam)}')


def glavni_meni():
    while True:
        print('''
        Kaj bi rad naredil?
        1) dodal preliv
        2) dodal račun
        3) dodal kuverto
        4) pogledal stanje
        5) šel iz programa
        ''')
        izbira = input('> ')
        if izbira == '1':
            dodaj_preliv()
        elif izbira == '2':
            dodaj_racun()
        elif izbira == '3':
            dodaj_kuverto()
        elif izbira == '4':
            poglej_stanje()
        elif izbira == '5':
            print('Nasvidenje!')
            break
        else:
            print('Neveljavna izbira')

def dodaj_preliv():
    znesek = vnesi_stevilo('Znesek> ')
    datum = date.today()
    opis = input('Opis> ')
    print('Račun:')
    racun = izberi(proracun.racuni)
    print('Kuverta:')
    kuverta = izberi(proracun.kuverte)
    proracun.dodaj_preliv(znesek, datum, opis, racun, kuverta)
    print('Preliv uspešno dodan!')

def dodaj_racun():
    ime_racuna = input('Vnesi ime računa> ')
    proracun.dodaj_racun(ime_racuna)
    print('Račun uspešno dodan!')

def dodaj_kuverto():
    ime_kuverte = input('Vnesi ime kuverte> ')
    proracun.dodaj_racun(ime_kuverte)
    print('Kuverta uspešno dodana!')

def poglej_stanje():
    for racun in proracun.racuni:
        print(racun)


glavni_meni()