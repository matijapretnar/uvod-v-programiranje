def stevilo_vrstic(ime_datoteke):
    stevilo = 0
    with open(ime_datoteke) as datoteka:
        for vrstica in datoteka:
            stevilo += 1
        return stevilo

def stevilo_znakov(ime_datoteke):
    stevilo = 0
    with open(ime_datoteke) as datoteka:
        for vrstica in datoteka:
            stevilo += len(vrstica)
        return stevilo


def stevilo_besed(ime_datoteke):
    stevilo = 0
    with open(ime_datoteke) as datoteka:
        for vrstica in datoteka:
            besede = vrstica.split()
            stevilo += len(besede)
        return stevilo


def ostevilci(ime_datoteke):
    stevilka_vrstice = 1
    ime_izhodne_datoteke = 'ostevilcena-' + ime_datoteke
    with open(ime_datoteke) as datoteka:
        with open(ime_izhodne_datoteke, 'w') as izhodna_datoteka:
            for vrstica in datoteka:
                print(stevilka_vrstice, vrstica, end='', file=izhodna_datoteka)
                stevilka_vrstice += 1


ostevilci('moji-stavki.txt')
