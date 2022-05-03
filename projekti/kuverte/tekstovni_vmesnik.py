from datetime import date
import model

stanje = model.primer

def preberi_stevilo(poziv="> "):
    while True:
        vnos = input(poziv)
        try:
            return int(vnos)
        except ValueError:
            print("Vnesti morate število.")


def izberi_moznost(moznosti):
    """Uporabniku našteje možnosti ter vrne izbrano."""
    for i, (_moznost, opis) in enumerate(moznosti, 1):
        print(f"{i}) {opis}")
    while True:
        i = preberi_stevilo()
        if 1 <= i <= len(moznosti):
            moznost, _opis = moznosti[i - 1]
            return moznost
        else:
            print(f"Vnesti morate število med 1 in {len(moznosti)}.")

def izberi_kuverto():
    moznosti = [(kuverta, kuverta.ime) for kuverta in stanje.kuverte]
    return izberi_moznost(moznosti)

def izberi_racun():
    moznosti = [(racun, racun.ime) for racun in stanje.racuni]
    return izberi_moznost(moznosti)

def pozdravno_sporocilo():
    print("Živjo!")

def zakljuci_izvajanje():
    print("Nasvidenje!")
    exit()

def prikazi_stanje():
    for kuverta in stanje.kuverte:
        print(kuverta)
    for racun in stanje.racuni:
        print(racun)

def ponudi_dejanja():
    print("Kaj bi rad naredil?")
    izbrano_dejanje = izberi_moznost([
        (prikazi_stanje, "prikaži stanje"),
        (zakljuci_izvajanje, "zaključi izvajanje"),
        (dodaj_transakcijo, "dodaj transakcijo")
    ])
    izbrano_dejanje()

def dodaj_transakcijo():
    opis = input("Opis> ")
    znesek = preberi_stevilo("Znesek> ")
    datum = date.today()
    kuverta = izberi_kuverto()
    racun = izberi_racun()
    transakcija = model.Transakcija(opis, znesek, datum)
    kuverta.dodaj_transakcijo(transakcija)
    racun.dodaj_transakcijo(transakcija)

def tekstovni_vmesnik():
    pozdravno_sporocilo()
    while True:
        ponudi_dejanja()

tekstovni_vmesnik()