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