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

def osnovni_meni():
    print('Kaj bi rad naredil?')
    print('1) dodaj vprašanje')
    print('2) glasuj za trenutno vprašanje')
    print('3) odpri vprašanje')
    izbira = input('> ')
    if izbira == '1':
        dodaj_vprasanje()
    elif izbira == '2':
        glasuj_za_trenutno_vprasanje()
    elif izbira == '3':
        odpri_vprasanje()
    else:
        print('Izbrati moraš eno od zgornjih možnosti.')

def dodaj_vprasanje():
    print('Uspešno si dodal vprašanje.')

def glasuj_za_trenutno_vprasanje():
    besedilo = zbirka_vprasanj.besedilo_trenutnega_vprasanja()
    if besedilo == None:
        print('Trenutno ni odprtega vprašanja!')
    else:
        print(besedilo)
        for indeks, odgovor in enumerate(zbirka_vprasanj.trenutno_vprasanje.odgovori):
            print('{mesto}) {besedilo} ({glasovi_odgovora}/{vsi_glasovi})'.format(
                mesto=indeks + 1,
                besedilo=odgovor.besedilo,
                glasovi_odgovora=odgovor.stevilo_glasov(),
                vsi_glasovi=zbirka_vprasanj.trenutno_vprasanje.stevilo_glasov(),
            ))
        izbira = input('> ')
        indeks_odgovora = int(izbira) - 1
        zbirka_vprasanj.glasuj(indeks_odgovora)
        print('Uspešno si glasoval!')

def odpri_vprasanje():
    print('Uspešno si odprl vprašanje.')

def main():
    pozdrav()
    while True:
        osnovni_meni()

main()
