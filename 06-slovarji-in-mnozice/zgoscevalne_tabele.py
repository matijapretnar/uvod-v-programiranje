def prazna_mnozica(n=8):
    return {"st_elementov": 0, "skatle": [[] for _ in range(n)]}


def poisci_skatlo(mnozica, n):
    skatle = mnozica["skatle"]
    return skatle[n % len(skatle)]


def dodaj_brez_preurejanja(mnozica, n):
    mnozica["st_elementov"] += 1
    poisci_skatlo(mnozica, n).append(n)


def dodaj(mnozica, n):
    dodaj_brez_preurejanja(mnozica, n)
    if mnozica["st_elementov"] > 2 / 3 * len(mnozica["skatle"]):
        print(f"preurejam {mnozica['st_elementov']} {len(mnozica['skatle'])}")
        preuredi(mnozica)
        print(f"končano")


def preuredi(mnozica):
    nova_mnozica = prazna_mnozica(n=2 * len(mnozica["skatle"]))
    for skatla in mnozica["skatle"]:
        for n in skatla:
            dodaj_brez_preurejanja(nova_mnozica, n)
    mnozica["skatle"] = nova_mnozica["skatle"]


def ali_obstaja(mnozica, n):
    return n in poisci_skatlo(mnozica, n)


m = prazna_mnozica()
for x in range(10000000):
    dodaj(m, x)