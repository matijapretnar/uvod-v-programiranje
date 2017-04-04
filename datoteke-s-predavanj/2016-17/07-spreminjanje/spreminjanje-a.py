def stevilo_sodih_elementov(seznam):
    stevec_sodih = 0
    for element in seznam:
        if element % 2 == 0:
            stevec_sodih += 1
    return stevec_sodih

def sodi_elementi(seznam):
    seznam_sodih = []
    for element in seznam:
        if element % 2 == 0:
            seznam_sodih.append(element)
    return seznam_sodih


def delne_vsote(seznam):
    '''Vrne seznam delnih vsot.

    >>> delne_vsote([1, 2, 10, 5, 7, 6])
    [1, 3, 13, 18, 25, 31]
    '''
    seznam_delnih_vsot = []
    delna_vsota = 0
    for element in seznam:
        delna_vsota += element
        seznam_delnih_vsot.append(delna_vsota)
    return seznam_delnih_vsot

def stevilo_crk(niz):
    stevil
    
