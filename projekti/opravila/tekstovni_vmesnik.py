from datetime import date
from model import Stanje, Kategorija, Opravilo

stanje = Stanje(
    [
        Kategorija(
            "služba",
            [
                Opravilo("povej, da ne smejo prepisovati", True),
                Opravilo("odpredavaj tekstovni vmesnik", False),
            ],
        ),
        Kategorija("doma", [Opravilo("zalij rože", False)]),
        Kategorija("gasilci", [Opravilo("povej, da rabiš cisterno zaradi rož", True)]),
    ]
)


def preberi_stevilo():
    while True:
        vnos = input("> ")
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


def prikaz_kategorije(kategorija):
    neopravljena = kategorija.stevilo_neopravljenih()
    return f"{kategorija.ime.upper()} ({neopravljena})"


def prikaz_opravila(opravilo):
    if opravilo.opravljeno:
        return f"☑︎ {opravilo.opis}"
    else:
        return f"☐ {opravilo.opis}"


def izberi_kategorijo(stanje):
    print("Izberite kategorijo:")
    return izberi_moznost(
        [
            (kategorija, prikaz_kategorije(kategorija))
            for kategorija in stanje.kategorije
        ]
    )


def izberi_opravilo(kategorija):
    print("Izberite opravilo:")
    return izberi_moznost(
        [(opravilo, prikaz_opravila(opravilo)) for opravilo in kategorija.opravila]
    )


def zacetni_pozdrav():
    print("Pozdravljeni v programu za vodenje opravil!")


def dodaj_kategorijo():
    print("Vnesite podatke nove kategorije.")
    ime = input("Ime> ")
    nova_kategorija = Kategorija(ime, [])
    stanje.dodaj_kategorijo(nova_kategorija)


def dodaj_opravilo():
    kategorija = izberi_kategorijo(stanje)
    print("Vnesite podatke novega opravila.")
    opis = input("Opis> ")
    novo_opravilo = Opravilo(opis)
    kategorija.dodaj_opravilo(novo_opravilo)


def opravi_opravilo():
    kategorija = izberi_kategorijo(stanje)
    opravilo = izberi_opravilo(kategorija)
    opravilo.opravi()


def izpisi_trenutno_stanje():
    for kategorija in stanje.kategorije:
        print(f"{prikaz_kategorije(kategorija)}:")
        for opravilo in kategorija.opravila:
            print(f"  {prikaz_opravila(opravilo)}")
    if not stanje.kategorije:
        print(
            "Trenutno nimate še nobene kategorije, zato morate eno najprej ustvariti."
        )


def zakljuci_izvajanje():
    print("Nasvidenje!")
    exit()


def ponudi_moznosti():
    print("Kaj bi radi naredili?")
    izbrano_dejanje = izberi_moznost(
        [
            (dodaj_kategorijo, "dodal novo kategorijo"),
            (dodaj_opravilo, "dodal novo opravilo"),
            (opravi_opravilo, "opravil opravilo"),
            (zakljuci_izvajanje, "odšel iz programa"),
        ]
    )
    izbrano_dejanje()


def tekstovni_vmesnik():
    zacetni_pozdrav()
    while True:
        izpisi_trenutno_stanje()
        ponudi_moznosti()


tekstovni_vmesnik()
