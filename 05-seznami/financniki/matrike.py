def sled(mat):
    '''Vrne sled matrike mat.'''
    vsota = 0

    for k in range(len(mat)):
        vsota += mat[k][k]

    return vsota

def nicelna_matrika(n):
    '''Vrne ničelno matriko velikosti n x n.'''
    mat = []
    for _ in range(n):
        vrstica = n * [0]
        mat.append(vrstica)
    return mat


def identicna_matrika(n):
    '''Vrne identično matriko velikosti n x n.'''
    mat = nicelna_matrika(n)

    for k in range(len(mat)):
        mat[k][k] = 1

    return mat
