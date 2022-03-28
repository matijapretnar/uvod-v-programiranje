def je_samoglasnik(niz):
    return len(niz) == 1 and niz.lower() in 'aeiou'


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

def najvecji_kljuc(slovar):
    najvecji = None
    for kljuc in slovar:
        if najvecji == None or kljuc > najvecji:
            najvecji = kljuc
    return najvecji

def najvecja_vrednost(slovar):
    najvecja = None
    for kljuc in slovar:
        if najvecja == None or slovar[kljuc] > najvecja:
            najvecja = slovar[kljuc]
    return najvecja

def kljuc_najvecje_vrednosti(slovar):
    kljuc_najvecje = None
    for trenutni_kljuc in slovar:
        if kljuc_najvecje == None or slovar[trenutni_kljuc] > slovar[kljuc_najvecje]:
            kljuc_najvecje = trenutni_kljuc
    return kljuc_najvecje

def kljuc_najvecje_vrednosti(slovar):
    najvecja = None
    kljuc_najvecje = None
    for trenutni_kljuc, trenutna_vrednost in slovar.items():
        if kljuc_najvecje == None or trenutna_vrednost > najvecja:
            najvecja = trenutna_vrednost
            kljuc_najvecje = trenutni_kljuc
    return kljuc_najvecje
