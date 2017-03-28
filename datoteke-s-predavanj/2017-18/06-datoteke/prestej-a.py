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
