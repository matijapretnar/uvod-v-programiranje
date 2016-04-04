def sled(matrika):
    '''Vrne sled dane matrike.'''
    vsota = 0
    for k in range(len(matrika)):
        vsota += matrika[k][k]
    return vsota


def nicelna_matrika(n):
    '''Vrne ničelno matriko velikosti n x n.'''
    return [n * [0] for _ in range(n)]


def identicna_matrika(n):
    matrika = nicelna_matrika(n)
    for k in range(n):
        matrika[k][k] = 1
    return matrika
