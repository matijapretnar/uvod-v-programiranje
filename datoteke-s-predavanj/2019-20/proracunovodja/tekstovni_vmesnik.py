from datetime import date
from model import Proracun

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
DATOTEKA_S_STANJEM = 'stanje.json'

try:
    proracun = Proracun.nalozi_stanje(DATOTEKA_S_STANJEM)
except:
    proracun = Proracun()

# Pomožne funkcije za vnos

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

def vnesi_stevilo(pozdrav):
    """S standardnega vhoda prebere naravno število."""
    while True:
        try:
            stevilo = input(pozdrav)
            return int(stevilo)
        except ValueError:
            print(slabo(f'Prosim, da vnesete število!'))


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
    return izberi([(prikaz_racuna(racun), racun) for racun in proracun.racuni])



# Sestavni deli uporabniškega vmesnika


def glavni_meni():
    print(krepko(LOGO))
    print(krepko('Pozdravljeni v programu računovodja!'))
    print('Za izhod pritisnite Ctrl-C.')
    while True:
        try:
            print(80 * '=')
            povzetek_stanja()
            print()
            print(krepko('Kaj bi radi naredili?'))
            moznosti = [
                ('vnesel priliv/odliv', dodaj_preliv),
                ('prenesel denar med kuvertama', prenesi_denar),
                ('dodal nov račun', dodaj_racun),
                ('dodal novo kuverto', dodaj_kuverto),
                ('odstranil kuverto', odstrani_kuverto),
                ('pogledal stanje', poglej_stanje),
            ]
            izbira = izberi(moznosti)
            print(80 * '-')
            izbira()
            print()
            input('Pritisnite Enter za shranjevanje in vrnitev v osnovni meni...')
            proracun.shrani_stanje(DATOTEKA_S_STANJEM)
        except ValueError as e:
            print(slabo(e.args[0]))
        except KeyboardInterrupt:
            print()
            print('Nasvidenje!')
            return


def povzetek_stanja():
    for kuverta in proracun.kuverte:
        stanje_kuverte = kuverta.stanje()
        if stanje_kuverte < 0:
            print(slabo(f'V kuverti {kuverta.ime} je {-stanje_kuverte} € premalo!'))
    nerazporejena_sredstva = proracun.nerazporejena_sredstva()
    if nerazporejena_sredstva > 0:
        print(dobro(f'Razporedite lahko še {nerazporejena_sredstva} €'))
    elif nerazporejena_sredstva < 0:
        print(slabo(f'Razporedili ste {-nerazporejena_sredstva} € preveč!'))


def dodaj_preliv():
    znesek = vnesi_stevilo('Znesek> ')
    datum = date.today().strftime('%Y-%m-%d')
    opis = input('Opis> ')
    print('Račun:')
    racun = izberi_racun(proracun.racuni)
    print('Kuverta:')
    kuverta = izberi_kuverto([None] + proracun.kuverte)
    proracun.nov_preliv(znesek, datum, opis, racun, kuverta)
    print(dobro('Preliv uspešno dodan!'))


def prenesi_denar():
    print('Od kod bi prenesli denar?')
    kuverte_s_prazno = [None] + proracun.kuverte
    kuverta1 = izberi_kuverto(kuverte_s_prazno)
    print('Kam bi prenesli denar?')
    kuverta2 = izberi_kuverto([kuverta for kuverta in kuverte_s_prazno if kuverta != kuverta1])
    znesek = vnesi_stevilo('Znesek> ')
    proracun.premakni_denar(kuverta1, kuverta2, znesek)
    print('Novo stanje:')
    print(f'- {prikaz_kuverte(kuverta1)}')
    print(f'- {prikaz_kuverte(kuverta2)}')


def dodaj_racun():
    ime_racuna = input('Vnesi ime računa> ')
    proracun.nov_racun(ime_racuna)
    print(dobro('Račun uspešno dodan!'))


def dodaj_kuverto():
    ime_kuverte = input('Vnesi ime kuverte> ')
    proracun.nova_kuverta(ime_kuverte)
    print(dobro('Kuverta uspešno dodana!'))

def odstrani_kuverto():
    print('Izberite kuverto, ki bi jo radi izbrisali.')
    kuverta = izberi_kuverto(proracun.kuverte)
    if input(f'Ste prepričani, da želite odstraniti kuverto {kuverta.ime}? [da/NE]') == 'da':
        proracun.odstrani_kuverto(kuverta)
        print(dobro('Kuverta uspešno odstranjena!'))
    else:
        print('Odstranitev kuverte preklicana.')


def poglej_stanje():
    print(krepko('RAČUNI:'))
    for racun in proracun.racuni:
        print(f'- {prikaz_racuna(racun)}')
    print(krepko('KUVERTE:'))
    for kuverta in proracun.kuverte:
        print(f'- {prikaz_kuverte(kuverta)}')
    print(f'- {prikaz_kuverte(None)}')


glavni_meni()
