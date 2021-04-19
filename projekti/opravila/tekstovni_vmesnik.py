DODAJ_SPISEK = 1
POBRISI_SPISEK = 2
ZAMENJAJ_SPISEK = 3
DODAJ_OPRAVILO = 4
POBRISI_OPRAVILO = 5
OPRAVI_OPRAVILO = 6
IZHOD = 7


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


tekstovni_vmesnik()
