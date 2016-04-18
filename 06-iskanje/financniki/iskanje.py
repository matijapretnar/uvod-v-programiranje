def ali_se_pojavi(x, seznam):
    '''Vrne True, kadar se x pojavi v danem seznamu.'''
    for y in seznam:
        if x == y:
            return True
    return False


def pripadajoca_vrednost(iskani_kljuc, seznam):
    '''Vrne vrednost, ki pripada ključu v danem seznamu parov.'''
    for kljuc, vrednost in seznam:
        if kljuc == iskani_kljuc:
            return vrednost
    return None


def ali_se_pojavi_v_urejenem_napacen(x, seznam):    # T(n)
    '''Vrne True, kadar se x pojavi v danem urejenem seznamu.'''
    # T(n / 2) + O(n / 2)
    # O(1)
    if len(seznam) == 0:  # O(1)
        return False      # O(1)
    elif len(seznam) == 1:  # O(1)
        return seznam[0] == x  # O(1)
    else:
      # O(1) + T(n / 2) + O(n / 2) = T(n / 2) + O(n / 2)
        # O(1)
        indeks_sredine = len(seznam) // 2  # O(1)
        sredina = seznam[indeks_sredine]   # O(1)

        # T(n / 2) + O(n / 2)
        if x == sredina:                   # O(1)
            return True                    # O(1)
        elif x < sredina:                  # O(1)
            # T(n / 2) + O(n / 2)
            return ali_se_pojavi_v_urejenem_napacen(x, seznam[:indeks_sredine])
        elif x > sredina:
            # T(n / 2) + O(n / 2)
            return ali_se_pojavi_v_urejenem_napacen(x, seznam[indeks_sredine + 1:])

def ali_se_pojavi_v_urejenem(x, seznam, zac, kon):
    '''Vrne True, kadar se x pojavi v danem urejenem seznamu med indeksoma zac in kon.'''
    if kon - zac == 0:
        return False
    elif kon - zac == 1:
        return seznam[zac] == x
    else:
        indeks_sredine = (zac + kon) // 2  # O(1)
        sredina = seznam[indeks_sredine]   # O(1)

        # T(n / 2) + O(n / 2)
        if x == sredina:                   # O(1)
            return True                    # O(1)
        elif x < sredina:                  # O(1)
            # T(n / 2) + O(n / 2)
            return ali_se_pojavi_v_urejenem(x, seznam, zac, indeks_sredine)
        elif x > sredina:
            # T(n / 2) + O(n / 2)
            return ali_se_pojavi_v_urejenem(x, seznam, indeks_sredine + 1, kon)












def ali_se_pojavi_v_urejenem(x, seznam, zac=0, kon=None):
    '''Vrne True, kadar se x pojavi v seznamu, in False, kadar se ne.'''
    if kon is None:
        kon = len(seznam)
    if zac == kon:
        return False

    sredina = (kon + zac) // 2

    if x == seznam[sredina]:
        return True

    elif x < seznam[sredina]:
        return ali_se_pojavi_v_urejenem(x, seznam, zac, sredina)

    elif x > seznam[sredina]:
        return ali_se_pojavi_v_urejenem(x, seznam, sredina + 1, kon)
