def prestej_samoglasnike_rek(niz, i=0):
    """Prešteje vse samoglasnike v nizu od indeksa i naprej"""
    if i >= len(niz):
        return 0
    elif niz[i].lower() in "aeiou":
        return 1 + prestej_samoglasnike_rek(niz, i + 1)
    else:
        return prestej_samoglasnike_rek(niz, i + 1)


def prestej_samoglasnike_for(niz, i=0):
    """Prešteje vse samoglasnike v nizu od indeksa i naprej"""
    stevec = 0
    for j in range(i, len(niz)):
        if niz[j].lower() in "aeiou":
            stevec += 1
    return stevec


def prestej_samoglasnike(niz):
    """Prešteje vse samoglasnike v nizu"""
    stevec = 0
    for j in range(len(niz)):
        if niz[j].lower() in "aeiou":
            stevec += 1
    return stevec


def prestej_samoglasnike(niz):
    """Prešteje vse samoglasnike v nizu"""
    stevec = 0
    for znak in niz:
        if znak.lower() in "aeiou":
            stevec += 1
    return stevec
