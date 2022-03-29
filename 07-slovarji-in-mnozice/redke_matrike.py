from prestej import kljuc_najvecje_vrednosti

navadna = [
    [1, 1, 4, 1, 1, 1, 1, 1, 1, 1],
    [5, 2, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 3, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 4, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

redka = (6, 10, 1, {(0, 2): 4, (1, 0): 5, (1, 1): 2, (2, 4): 3, (4, 2): 4})


def iz_redke_v_navadno(redka):
    st_vrstic, st_stolpcev, vecinski, izjeme = redka
    navadna = []
    for i in range(st_vrstic):
        vrstica = []
        for j in range(st_stolpcev):
            vrstica.append(izjeme.get((i, j), vecinski))
        navadna.append(vrstica)
    return navadna


def prestej_elemente_matrike(matrika):
    pojavitve = {}
    for vrstica in matrika:
        for element in vrstica:
            pojavitve[element] = pojavitve.get(element, 0) + 1
    return pojavitve


def iz_navadne_v_redko(navadna):
    st_vrstic = len(navadna)
    st_stolpcev = len(navadna[0])
    vecinski = kljuc_najvecje_vrednosti(prestej_elemente_matrike(navadna))
    izjeme = {}
    for i, vrstica in enumerate(navadna):
        for j, element in enumerate(vrstica):
            if element != vecinski:
                izjeme[(i, j)] = element
    return (st_vrstic, st_stolpcev, vecinski, izjeme)


print(iz_redke_v_navadno(redka))
print(iz_redke_v_navadno(redka) == navadna)
print(iz_navadne_v_redko(navadna))
print(iz_navadne_v_redko(navadna) == redka)
