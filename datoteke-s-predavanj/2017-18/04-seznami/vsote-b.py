vsota_elementov_najbolj_lena = sum


def vsota_elementov_lena(seznam):
    return sum(seznam)


def vsota_elementov_rekurzija(seznam):
    if len(seznam) == 0:
        return 0
    else:
        return seznam[0] + vsota_elementov_rekurzija(seznam[1:])


def vsota_elementov_boljsa_rekurzija(seznam, i=0):
    if i >= len(seznam):
        return 0
    else:
        return seznam[i] + vsota_elementov_boljsa_rekurzija(seznam, i + 1)


def vsota_z_bisekcijo(seznam, i=0, j=None):
    if j is None:
        j = len(seznam)
    if i >= j:
        return 0
    elif i == j - 1:
        return seznam[i]
    else:
        k = (i + j) // 2
        leva_polovica = vsota_z_bisekcijo(seznam, i, k)
        desna_polovica = vsota_z_bisekcijo(seznam, k, j)
        return leva_polovica + desna_polovica


def vsota_elementov_zanka1(seznam):
    vsota = 0
    for x in seznam:
        vsota += x
    return vsota


def vsota_elementov_zanka2(seznam):
    vsota = 0
    for i in range(len(seznam)):
        vsota += seznam[i]
    return vsota


def vsota_elementov_zanka3(seznam):
    vsota = 0
    i = 0
    while i < len(seznam):
        vsota += seznam[i]
        i += 1
    return vsota
