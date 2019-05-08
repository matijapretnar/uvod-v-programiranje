from model import ZbirkaVprasanj, Vprasanje, Odgovor

zbirka_vprasanj = ZbirkaVprasanj(ime='UVP 2018/19', vprasanja=[
    Vprasanje('Kakšno je danes vreme?', [
        Odgovor('sončno'),
        Odgovor('oblačno'),
        Odgovor('deževno'),
    ])
])
zbirka_vprasanj.odpri_vprasanje(0)

SIRINA_VRSTICE = 40
SIRINA_GRAFA = 16


def napaka(niz):
    print('\033[1;91m' + niz + '\033[0m')


def uspeh(niz):
    print('\033[1;94m' + niz + '\033[0m')


def male_stevke(n):
    return ''.join('₀₁₂₃₄₅₆₇₈₉'[int(stevka)] for stevka in str(n))


def narisi_delez(m, n, max_dolzina=SIRINA_GRAFA):
    if n == 0:
        stolpec = ''
    else:
        stolpec = round(max_dolzina * m / n) * '═'
    return '╞' + stolpec.ljust(max_dolzina)


def preberi():
    return input('> ')


def preberi_stevilo():
    while True:
        izbira = preberi()
        if izbira.isdigit():
            return int(izbira)
        else:
            napaka('Vpišite številko')


def preberi_seznam():
    seznam = []
    while True:
        seznam.append(preberi())
        if seznam[-1] == '':
            return seznam[:-1]


def izberi(moznosti):
    for i, (oznaka, _) in enumerate(moznosti, 1):
        print(f'{i}) {oznaka}')
    while True:
        izbira = preberi_stevilo()
        if 1 <= izbira <= len(moznosti):
            return moznosti[izbira - 1][1]
        else:
            napaka(f'Vpišite številko med 1 in {len(moznosti)}')


def izberi_indeks(oznake):
    return izberi([(oznaka, i) for (i, oznaka) in enumerate(oznake)])


def prikaz_odgovorov(odgovori):
    dolzina_najdaljsega_odgovora = max(len(odgovor.besedilo) for odgovor in odgovori)
    stevilo_vseh_glasov = sum(odgovor.stevilo_glasov() for odgovor in odgovori)
    for odgovor in odgovori:
        poravnano_besedilo = odgovor.besedilo.ljust(dolzina_najdaljsega_odgovora)
        stevilo_glasov = odgovor.stevilo_glasov()
        graf = narisi_delez(stevilo_glasov, stevilo_vseh_glasov)
        yield f'{poravnano_besedilo} {graf} ₍{male_stevke(stevilo_glasov)}₎'


def prikazi_trenutno_vprasanje():
    vprasanje = zbirka_vprasanj.trenutno_vprasanje
    if vprasanje is None:
        napaka('Trenutno ni odprtega vprašanja.')
    else:
        uspeh('Trenutno vprašanje:')
        print(vprasanje.besedilo)
        for odgovor in prikaz_odgovorov(vprasanje.odgovori):
            print('  - {}'.format(odgovor))


def osnovni_meni():
    print(SIRINA_VRSTICE * '═')
    prikazi_trenutno_vprasanje()
    mozni_koraki = [
        ('dodaj vprašanje', dodaj_vprasanje),
        ('odpri vprašanje', odpri_vprasanje),
        ('podvoji vprašanje', podvoji_vprasanje),
    ]
    if zbirka_vprasanj.trenutno_vprasanje is not None:
        mozni_koraki += [
            ('glasuj za trenutno vprašanje', glasuj_za_trenutno_vprasanje),
            ('zapri trenutno vprašanje', zapri_trenutno_vprasanje),
        ]
    print(SIRINA_VRSTICE * '─')
    print('Kaj bi rad naredili?')
    naslednji_korak = izberi(mozni_koraki)
    naslednji_korak()


def dodaj_vprasanje():
    print('Kakšno naj bo besedilo vprašanja?')
    vprasanje = preberi()
    print('Vpišite vse možne odgovore. Vnos zaključite s prazno vrstico.')
    odgovori = preberi_seznam()
    zbirka_vprasanj.dodaj_vprasanje(vprasanje, odgovori)
    uspeh('Uspešno ste dodali vprašanje.')


def odpri_vprasanje():
    print('Katero vprašanje želite odpreti?')
    indeks_vprasanja = izberi_indeks(vprasanje.besedilo for vprasanje in zbirka_vprasanj.vprasanja)
    zbirka_vprasanj.odpri_vprasanje(indeks_vprasanja)
    uspeh('Uspešno ste odprli vprašanje.')


def podvoji_vprasanje():
    print('Katero vprašanje želite podvojiti?')
    indeks_vprasanja = izberi_indeks(vprasanje.besedilo for vprasanje in zbirka_vprasanj.vprasanja)
    zbirka_vprasanj.podvoji_vprasanje(indeks_vprasanja)
    uspeh('Uspešno ste podvojili vprašanje.')


def glasuj_za_trenutno_vprasanje():
    vprasanje = zbirka_vprasanj.trenutno_vprasanje
    print(vprasanje.besedilo)
    indeks_odgovora = izberi_indeks(prikaz_odgovorov(vprasanje.odgovori))
    zbirka_vprasanj.glasuj(indeks_odgovora)
    uspeh('Uspešno ste glasovali!')


def zapri_trenutno_vprasanje():
    zbirka_vprasanj.zapri_trenutno_vprasanje()
    uspeh('Vprašanje zaprto!')


def main():
    uspeh('Pozdravljeni v programu ???')
    while True:
        osnovni_meni()


main()
