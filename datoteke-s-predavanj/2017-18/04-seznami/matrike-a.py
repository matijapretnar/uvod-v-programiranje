def vsota_matrike(matrika):
    vsota = 0
    for vrstica in matrika:
        print('Prištevam vrstico', vrstica)
        for element in vrstica:
            print('Prištevam element', element)
            vsota += element
    return vsota


def sled_matrike(matrika):
    sled = 0
    for i in range(len(matrika)):
        sled += matrika[i][i]
    return sled


def bedna_sled_matrike(matrika):
    sled = 0
    for i in range(len(matrika)):
        for j in range(len(matrika)):
            if i == j:
                sled += matrika[i][j]
    return sled
