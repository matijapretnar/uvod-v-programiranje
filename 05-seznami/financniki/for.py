def najvecji_element(sez):
    '''Vrne največji element seznama sez. če je prazen, vrne None.'''
    if len(sez) == 0:
        return

    najvecji_do_zdaj = sez[0]

    for x in sez:
        if x > najvecji_do_zdaj:
            najvecji_do_zdaj = x

    return najvecji_do_zdaj


def najvecja_vrednost(sez, f):
    '''Vrne element seznama sez, pri katerem f doseže največjo vrednost.'''
    if len(sez) == 0:
        return

    argument_najvecje_vrednosti = sez[0]
    najvecja_vrednost_do_zdaj = f(sez[0])

    for x in sez:
        y = f(x)
        if y > najvecja_vrednost_do_zdaj:
            argument_najvecje_vrednosti = x
            najvecja_vrednost_do_zdaj = y

    return argument_najvecje_vrednosti


def pozitivni_elementi(sez):
    '''Vrne seznam vseh pozitivnih elementov seznama sez.'''
    pozitivni = []
    for x in sez:
        if x > 0:
            pozitivni.append(x)
    return pozitivni

# največje število med 1 in 1000000, ki da enak ostanek pri deljenju s 47 in 513