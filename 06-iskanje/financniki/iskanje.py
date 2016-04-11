def ali_se_pojavi(x, seznam):
    '''Vrne True, kadar se x pojavi v danem seznamu.'''
    for y in seznam:
        if x == y:
            return True
    return False


def ali_se_pojavi_v_urejenem(x, seznam):
    '''Vrne True, kadar se x pojavi v danem urejenem seznamu.'''
    if len(seznam) == 0:
        return False
    elif len(seznam) == 1:
        return seznam[0] == x
    else:
        indeks_sredine = len(seznam) // 2
        sredina = seznam[indeks_sredine]
        if x == sredina:
            return True
        elif x < sredina:
            return ali_se_pojavi_v_urejenem(x, seznam[:indeks_sredine])
        elif x > sredina:
            return ali_se_pojavi_v_urejenem(x, seznam[indeks_sredine + 1:])


def pripadajoca_vrednost(iskani_kljuc, seznam):
    '''Vrne vrednost, ki pripada ključu v danem seznamu parov.'''
    for kljuc, vrednost in seznam:
        if kljuc == iskani_kljuc:
            return vrednost
    return None
