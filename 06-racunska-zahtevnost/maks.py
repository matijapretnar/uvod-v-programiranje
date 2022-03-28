import stopaj


def najvecji_element1(sez):
    maksi, maksi_i = None, None
    for i, x in enumerate(sez):
        if maksi is None or x > maksi:
            maksi = x
            maksi_i = i
    return maksi_i


def najvecji_element2(sez):
    for i, x in enumerate(sez):
        if x == max(sez):
            return i


def najvecji_element3(sez):
    maks = max(sez)
    for i, x in enumerate(sez):
        if x == maks:
            return i


stopaj.izmeri_case_poskusov(
    [stopaj.nakljucen_narascajoc_seznam(100 * n) for n in range(1, 20)],
    [najvecji_element1, najvecji_element3],
)
