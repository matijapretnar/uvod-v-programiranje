from model import Model, Kuverta, Racun, Transakcija
from datetime import date

eden_in_edini_model = Model()
hrana = Kuverta('hrana')
racuni = Kuverta('računi')
zabava = Kuverta('zabava')
gotovina = Racun('gotovina')
tekoci_racun = Racun('tekoči račun')
eden_in_edini_model.dodaj_kuverto(hrana)
eden_in_edini_model.dodaj_kuverto(racuni)
eden_in_edini_model.dodaj_kuverto(zabava)
eden_in_edini_model.dodaj_racun(gotovina)
eden_in_edini_model.dodaj_racun(tekoci_racun)
zadnji_nakup = Transakcija(15, 'špageti in pivo', date(2021, 4, 12))
gotovina.dodaj_transakcijo(zadnji_nakup)
hrana.dodaj_transakcijo(zadnji_nakup)

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
    for kuverta in eden_in_edini_model.kuverte:
        print(f'- {kuverta.ime}: {kuverta.stanje()}')


tekstovni_vmesnik()