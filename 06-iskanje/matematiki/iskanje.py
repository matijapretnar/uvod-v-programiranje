def poisci_v_neurejenem(seznam, x):
    '''Vrne True, kadar se x pojavi v seznamu, in False, kadar se ne.'''
    for y in seznam:
        if x == y:
            return True
    return False


def poisci_vrednost_v_neurejenem(seznam, iskani_kljuc):
    '''Vrne pripadajočo vrednost ključa v seznamu. Ce je ni, vrne None.'''
    for kljuc, vrednost in seznam:
        if iskani_kljuc == kljuc:
            return vrednost
    return None

# T(n)
def poisci_v_urejenem(seznam, x):
    '''Vrne True, kadar se x pojavi v seznamu, in False, kadar se ne.'''

    # O(1)
    if len(seznam) == 0:
        return False

    # O(1)
    sredina = len(seznam) // 2


       # O(1)
    if x == seznam[sredina]:
        # O(1)
        return True

         # O(1)
    elif x < seznam[sredina]:

               # T(n / 2) + O(n)
        return poisci_v_urejenem(seznam[:sredina], x)

    elif x > seznam[sredina]:
        return poisci_v_urejenem(seznam[sredina + 1:], x)
