def prestej_vrstice(ime_datoteke):
    stevilo_vrstic = 0
    with open(ime_datoteke) as datoteka:
        for vrstica in datoteka:
            stevilo_vrstic += 1
    return stevilo_vrstic

def prestej_znake(ime_datoteke):
    stevilo_znakov = 0
    with open(ime_datoteke) as datoteka:
        for vrstica in datoteka:
            stevilo_znakov += len(vrstica)
    return stevilo_znakov

def prestej_besede(ime_datoteke):
    stevilo_besed = 0
    with open(ime_datoteke) as datoteka:
        for vrstica in datoteka:
            stevilo_besed += len(vrstica.split())
    return stevilo_besed

def ostevilci_vrstice(ime_datoteke):
    ime_izhodne_datoteke = 'ostevilcena-' + ime_datoteke
    stevilka_vrstice = 1
    with open(ime_datoteke) as vhodna, open(ime_izhodne_datoteke, 'w') as izhodna:
        for vrstica in vhodna:
            if vrstica != '\n':
                print(stevilka_vrstice, vrstica, file=izhodna, end='')
                stevilka_vrstice += 1
            else:
                print('\n', end='', file=izhodna)
