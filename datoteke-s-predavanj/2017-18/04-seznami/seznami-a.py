def povprecje(seznam):
    if len(seznam) == 0:
        return None
    else:
        return sum(seznam) / len(seznam)


def povprecje(seznam):
    if seznam:
        return sum(seznam) / len(seznam)


def stevilo_elementov(seznam):
    stevec_elementov = 0
    for x in seznam:
        stevec_elementov += 1
    return stevec_elementov


def vsebuje_sodega(seznam):
    for x in seznam:
        if x % 2 == 0:
            return True
    return False


def vsebuje_samo_sode(seznam):
    for x in seznam:
        if x % 2 != 0:
            return False
    return True


def najvecji_element(seznam):
    if seznam:
        najvecji_do_zdaj = seznam[0]
        for x in seznam:
            if x > najvecji_do_zdaj:
                najvecji_do_zdaj = x
            print(x, najvecji_do_zdaj)
        return najvecji_do_zdaj


def najvecji_sodi_element(seznam):
    if seznam:
        najvecji_sodi_do_zdaj = seznam[0]
        for x in seznam:
            if x % 2 == 0 and x > najvecji_sodi_do_zdaj:
                najvecji_sodi_do_zdaj = x
        return najvecji_sodi_do_zdaj


def najvecji_sodi_element(seznam):
    najvecji_sodi_do_zdaj = None
    for x in seznam:
        x_je_sod = x % 2 == 0
        najvecjega_se_ni = najvecji_sodi_do_zdaj is None
        if x_je_sod and (najvecjega_se_ni or x > najvecji_sodi_do_zdaj):
            najvecji_sodi_do_zdaj = x
        print(x, najvecji_sodi_do_zdaj)
    return najvecji_sodi_do_zdaj
