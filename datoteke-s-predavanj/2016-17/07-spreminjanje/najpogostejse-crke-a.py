def seznam_besed(ime_datoteke):
    besede = []
    with open(ime_datoteke) as datoteka:
        for vrstica in datoteka:
            besede += vrstica.split()
    return besede

def pocisti_besede(besede):
    pociscene = []
    for beseda in besede:
        pociscene.append(beseda.replace(',', '').replace('.', '').lower())
    return pociscene

def prestej_pojavitve(besede):
    pojavitve = {}
    for beseda in besede:
        if beseda in pojavitve:
            pojavitve[beseda] += 1
        else:
            pojavitve[beseda] = 1
    return pojavitve

## Malo manj učinkovita rešitev
##def prestej_pojavitve2(besede):
##    pojavitve = {}
##    for beseda in besede:
##        if beseda not in pojavitve:
##            pojavitve[beseda] = besede.count(beseda)
##    return pojavitve

def najvecji_element(seznam):
    if seznam:
        najvecji_do_zdaj = seznam[0]
        for element in seznam:
            if element > najvecji_do_zdaj:
                najvecji_do_zdaj = element
        return najvecji_do_zdaj

def kljuc_z_najvecjo_vrednostjo(slovar):
    if slovar:
        max_kljuc = None
        for kljuc in slovar:
            if max_kljuc is None or slovar[kljuc] > slovar[max_kljuc]:
                max_kljuc = kljuc
        return max_kljuc

def kljuci_z_najvecjimi_vrednostmi(slovar, stevilo_kljucev):
    '''
    >>> kljuci_z_najvecjimi_vrednostmi({'a': 10, 'b': 5, 'c': 30}, 2)
    [('c', 30), ('a', 10)]
    '''
    max_kljuci = []
    for korak in range(stevilo_kljucev):
        print(korak, slovar, max_kljuci)
        if slovar:
            kljuc = kljuc_z_najvecjo_vrednostjo(slovar)
            max_kljuci.append((kljuc, slovar[kljuc]))
            del slovar[kljuc]
        else:
            break
    return max_kljuci

    



            

