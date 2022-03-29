def je_samoglasnik(niz):
    return len(niz) == 1 and niz.lower() in "aeiou"


def stevilo_samoglasnikov(niz):
    samoglasniki = 0
    for crka in niz:
        if je_samoglasnik(crka):
            samoglasniki += 1
    return samoglasniki


def stevilo_posameznih_samoglasnikov(niz):
    samoglasniki = {}
    for crka in niz:
        mala_crka = crka.lower()
        if je_samoglasnik(crka):
            if mala_crka in samoglasniki:
                samoglasniki[mala_crka] += 1
            else:
                samoglasniki[mala_crka] = 1
    return samoglasniki


def stevilo_posameznih_soglasnikov(niz):
    soglasniki = {}
    for crka in niz:
        mala_crka = crka.lower()
        if not je_samoglasnik(crka):
            soglasniki[mala_crka] = soglasniki.get(mala_crka, 0) + 1
    return soglasniki
