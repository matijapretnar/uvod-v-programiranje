def ali_vsebuje(matrika, x):
    st_vrstic = len(matrika)
    for indeks_vrstice in range(st_vrstic):
        vrstica = matrika[indeks_vrstice]
        if x in vrstica:
            return True
    return False

def ali_vsebuje_rek(matrika, x):
    if matrika == []:
        return False
    elif x in matrika[0]:
        return True
    else:
        return ali_vsebuje_rek(matrika[1:], x)

def ali_vsebuje(matrika, x):
    st_vrstic = len(matrika)
    for i in range(st_vrstic):
        vrstica = matrika[i]
        for j in range(len(vrstica)):
            if vrstica[j] == x:
                return True
    return False

def ali_vsebuje(matrika, x):
    for vrstica in matrika:
        for j in range(len(vrstica)):
            if vrstica[j] == x:
                return True
    return False
