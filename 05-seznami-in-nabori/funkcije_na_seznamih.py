def produkt_rek(sez):
    if sez == []:
        return 1
    else:
        return sez[0] * produkt_rek(sez[1:])

def produkt_rek(sez, i=0):
    assert i >= 0
    if i == len(sez):
        return 1
    else:
        return sez[i] * produkt_rek(sez, i=i+1)


def produkt_range(sez):
    prod = 1
    for i in range(len(sez)):
        prod *= sez[i]
    return prod


def produkt(sez):
    prod = 1
    for x in sez:
        prod *= x
    return prod


def sled_matrike(mat):
    sled = 0
    for i in range(len(mat)):
        sled += mat[i][i]
    return sled


def narobe_napisana_sled_matrike(mat):
    sled = 0
    for i in range(len(mat)):
        for j in range(len(mat)):
            if i == j:
                sled += mat[i][j]
    return sled


def najvecji_element(sez):
    if sez == []:
        return None
    najvecji = sez[0]
    for x in sez:
        if x > najvecji:
            najvecji = x
    return najvecji


def najvecji_element(sez):
    najvecji = None
    for x in sez:
        if najvecji == None or x > najvecji:
            najvecji = x
    return najvecji


def ali_vsebuje(sez, x):
    for y in sez:
        if y == x:
            return True
    return False


def pocasni_sodi_elementi(sez):
    sodi = []
    for x in sez:
        if x % 2 == 0:
            sodi = sodi + [x]
    return sodi

def hitri_sodi_elementi(sez):
    sodi = []
    for x in sez:
        if x % 2 == 0:
            sodi.append(x)
    return sodi

def ne_vem_kako_hitri_sodi_elementi(sez):
    sodi = []
    for x in sez:
        if x % 2 == 0:
            sodi += [x]
    return sodi

def izpeljani_sodi_elementi(sez):
    return [x for x in sez if x % 2 == 0]

