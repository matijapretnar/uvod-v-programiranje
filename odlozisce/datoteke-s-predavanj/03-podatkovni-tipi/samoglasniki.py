def stevilo_samoglasnikov(niz):
    if niz == '':
        return 0
    elif niz[0] in 'aeiouAEIOU':
        return 1 + stevilo_samoglasnikov(niz[1:])
    else:
        return stevilo_samoglasnikov(niz[1:])

def stevilo_samoglasnikov_brez_rezin(niz, od=0, do=None):
    """Vrne število samoglasnikov v niz[od:do]"""
    if do is None:
        do = len(niz)
    if od == do:
        return 0
    elif niz[od] in 'aeiouAEIOU':
        return 1 + stevilo_samoglasnikov_brez_rezin(niz, od + 1, do)
    else:
        return stevilo_samoglasnikov_brez_rezin(niz, od + 1, do)
