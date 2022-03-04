def je_podniz(podniz, niz):
    """Vrne True natanko tedaj, kadar se podniz pojavi v nizu (ne nujno strnjeno)"""
    if podniz in niz:
        return True
    if podniz == '':
        return True
    elif niz == '':
        return False
    # else:
    #     i = indeks_prve_pojavitve(podniz[0], niz)
    #     if i == None:
    #         return False
    #     else:
    #         return je_podniz(podniz[1:], niz[i + 1:])
    elif podniz[0] == niz[0]:
        return je_podniz(podniz[1:], niz[1:])
    else:
        return je_podniz(podniz, niz[1:])
    