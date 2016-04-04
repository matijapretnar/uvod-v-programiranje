def vsota_elementov(seznam):
    '''Vrne vsoto vseh elementov danega seznama.'''
    vsota = 0
    for element in seznam:
        vsota += element
    return vsota



def najvecji_element(seznam):
    '''Vrne največji element v danem seznamu.'''
    najvecji_do_zdaj = None
    for trenutni in seznam:
        if najvecji_do_zdaj is None or trenutni > najvecji_do_zdaj:
            najvecji_do_zdaj = trenutni
    return najvecji_do_zdaj


def pozitivni_elementi(seznam):
    '''Vrne seznam vseh pozitivnih elementov v danem seznamu.'''
    return [n for n in seznam if n > 0]


def pozitivni_elementi_z_metodami(seznam):
    '''Vrne seznam vseh pozitivnih elementov v danem seznamu.'''
    pozitivni = []
    for n in seznam:
        if n > 0:
            pozitivni.append(n)
    return pozitivni


