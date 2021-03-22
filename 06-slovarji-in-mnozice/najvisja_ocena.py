moje_ocene = {
    "Uvod v programiranje": 10,
    "Analiza 1": 5.9,
    "Algebra 1": 9,
    "Računalniški praktikum": 11,
    "Proseminar": 8,
    "Algebra 2": 6,
}


def najvisja_ocena(ocene):
    max_predmet = None
    max_ocena = 5
    for predmet, ocena in ocene.items():
        if ocena > max_ocena:
            max_predmet = predmet
            max_ocena = ocena
    return max_predmet, max_ocena


def najvecja_vrednost(slovar):
    max_k = None
    max_v = None
    for k, v in slovar.items():
        if max_v == None or v > max_v:
            max_k = k
            max_v = v
    return max_k, max_v
