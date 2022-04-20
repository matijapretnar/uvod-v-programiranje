import time

def ali_vsebuje(sez, x):
    for y in sez:
        if y == x:
            return True
    return False


def ali_vsebuje_urejen(sez, x, od, do):
    """Ali seznam sez vsebuje element x med indeksoma od in do"""
    if od >= do:
        return False
    indeks_srednjega = (od + do) // 2
    print("Računam...")
    srednji = sez[indeks_srednjega]
    if x > srednji:
        return ali_vsebuje_urejen(sez, x, indeks_srednjega + 1, do)
    elif x < srednji:
        return ali_vsebuje_urejen(sez, x, od, indeks_srednjega - 1)
    else:
        return True

def stopaj_koliko_casa_potrebuje(n):
    sez = [i for i in range(n)]
    zacetek = time.time()
    rezultat = ali_vsebuje_urejen(sez, -1, 0, len(sez) - 1)
    konec = time.time()
    print(f"n = {n}, cas = {konec - zacetek}s")
    return rezultat
