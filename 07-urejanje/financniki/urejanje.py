def zamenjaj(seznam, i, j):
    '''V danem seznamu zamenja elementa z indeksoma i in j.'''
    vmesna_vrednost = seznam[i]
    seznam[i] = seznam[j]
    seznam[j] = vmesna_vrednost

def uredi_z_vstavljanjem(seznam):
    '''Z algoritmom urejanja z vstavljanjem na mestu uredi dani seznam.'''
    for zacetek_neurejenega_dela in range(len(seznam) - 1):
        najmanjsi_v_neurejenem = zacetek_neurejenega_dela
        for k in range(zacetek_neurejenega_dela, len(seznam)):
            if seznam[k] < seznam[najmanjsi_v_neurejenem]:
                najmanjsi_v_neurejenem = k
        zamenjaj(seznam, zacetek_neurejenega_dela, najmanjsi_v_neurejenem)

    # v neurejenem delu poišči najmanjši element in ga postavi na pravo mesto

seznam = [10, 2, 4, 1, 5, 8, ]
uredi_z_vstavljanjem(seznam)