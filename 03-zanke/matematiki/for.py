def vsota_prvih_sodih_stevil(n):
    vsota = 0
    for stevilo in range(0, 2 * n + 1, 2):
        vsota += stevilo
    return vsota

vsota_prvih_sodih_stevil(5)


def fakulteta(n):
    '''Vrne fakulteto števila n.'''
    assert n >= 0

    produkt = 1
    for k in range(1, n + 1):
        produkt *= k
    return produkt

fakulteta(10)