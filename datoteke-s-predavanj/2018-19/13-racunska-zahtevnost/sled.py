import stopaj


def sled_matrike1(matrika):
    sled = 0
    for i, vrstica in enumerate(matrika):
        for j, element in enumerate(vrstica):
            if i == j:
                sled += element
    return sled


def sled_matrike2(matrika):
    sled = 0
    for i, vrstica in enumerate(matrika):
        sled += vrstica[i]
    return sled


def sled_matrike3(matrika):
    sled = 0
    for i in range(len(matrika)):
        sled += matrika[i][i]
    return sled


stopaj.izmeri_case_poskusov(
    [stopaj.nakljucna_matrika(50 * n) for n in range(1, 20)],
    [sled_matrike1, sled_matrike2, sled_matrike3],
)
