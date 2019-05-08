from model import ZbirkaVprasanj, Vprasanje, Odgovor

zbirka_vprasanj = ZbirkaVprasanj(ime='UVP 2018/19', vprasanja=[
    Vprasanje('Kakšno je danes vreme?', [
        Odgovor('sončno'),
        Odgovor('oblačno'),
        Odgovor('deževno'),
    ])
])
zbirka_vprasanj.odpri_vprasanje(0)


def pozdrav():
    print('Pozdravljen v programu ???')


def izberi(mozni_odgovori):
    for indeks, odgovor in enumerate(mozni_odgovori):
        print('{}) {}'.format(indeks + 1, odgovor))
    izbira = input('> ')
    return int(izbira) - 1


def osnovni_meni():
    print('Kaj bi rad naredil?')
    izbira = izberi([
        'dodaj vprašanje',
        'glasuj za trenutno vprašanje',
        'odpri vprašanje',
    ])
    if izbira == 0:
        dodaj_vprasanje()
    elif izbira == 1:
        glasuj_za_trenutno_vprasanje()
    elif izbira == 2:
        odpri_vprasanje()
    else:
        assert False


def dodaj_vprasanje():
    print('Uspešno si dodal vprašanje.')


def oznake_odgovorov(vprasanje):
    return [
        '{besedilo} ({glasovi_odgovora}/{vsi_glasovi})'.format(
            besedilo=odgovor.besedilo,
            glasovi_odgovora=odgovor.stevilo_glasov(),
            vsi_glasovi=vprasanje.stevilo_glasov(),
        ) for odgovor in vprasanje.odgovori
    ]


def glasuj_za_trenutno_vprasanje():
    vprasanje = zbirka_vprasanj.trenutno_vprasanje
    if vprasanje == None:
        print('Trenutno ni odprtega vprašanja!')
    else:
        print(vprasanje.besedilo)
        indeks_odgovora = izberi(oznake_odgovorov(vprasanje))
        zbirka_vprasanj.glasuj(indeks_odgovora)
        print('Uspešno si glasoval!')


def odpri_vprasanje():
    print('Uspešno si odprl vprašanje.')


def main():
    pozdrav()
    while True:
        osnovni_meni()


main()
