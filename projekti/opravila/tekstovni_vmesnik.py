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


def zacetni_pozdrav():
    print("Pozdravljen v programu za vodenje opravil.")


def izpisi_trenutno_stanje():
    for kategorija in stanje.kategorije:
        print(f"{kategorija.ime}: {kategorija.stevilo_neopravljenih()} neopravljenih")


def zakljuci_izvajanje():
    print("Adijo")
    exit()


def ponudi_moznosti():
    print("Kaj bi rad naredil?")
    izbrano_dejanje = izberi_moznost(
        [
            (izpisi_trenutno_stanje, "pogledal trenutno stanje"),
            (zakljuci_izvajanje, "odšel iz programa"),
        ]
    )
    izbrano_dejanje()


def tekstovni_vmesnik():
    zacetni_pozdrav()
    while True:
        ponudi_moznosti()


tekstovni_vmesnik()
