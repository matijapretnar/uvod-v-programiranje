from collections import defaultdict

def stevilo_posameznih_samoglasnikov(niz):
    samoglasniki = {}
    for crka in niz.lower():
        if crka in "aeiou":
            if crka in samoglasniki:
                samoglasniki[crka] += 1
            else:
                samoglasniki[crka] = 1
        print(crka, samoglasniki)
    return samoglasniki

def stevilo_posameznih_samoglasnikov(niz):
    samoglasniki = {}
    for crka in niz.lower():
        if crka in "aeiou":
            samoglasniki[crka] = samoglasniki.get(crka, 0) + 1
        print(crka, samoglasniki)
    return samoglasniki

def stevilo_posameznih_samoglasnikov(niz):
    samoglasniki = defaultdict(int)
    for crka in niz.lower():
        if crka in "aeiou":
            samoglasniki[crka] += 1
        print(crka, samoglasniki)
    return samoglasniki


def iz_navadne_v_redko(navadna):
    st_vrstic = len(navadna)
    st_stolpcev = len(navadna[0])
    pojavitve = {}
    for i, vrstica in enumerate(navadna):
        for j, element in enumerate(vrstica):
            if element in pojavitve:
                pojavitve[element].append((i, j))
            else:
                pojavitve[element] = [(i, j)]
    vecinski, _ = max(pojavitve.items(), key=lambda par: len(par[1]))
    del pojavitve[vecinski]
    izjeme = {
        mesto: vrednost
        for vrednost, mesta in pojavitve.items()
        for mesto in mesta
    }
    return (st_vrstic, st_stolpcev, vecinski, izjeme)

def iz_navadne_v_redko(navadna):
    st_vrstic = len(navadna)
    st_stolpcev = len(navadna[0])
    pojavitve = defaultdict(list)
    for i, vrstica in enumerate(navadna):
        for j, element in enumerate(vrstica):
            pojavitve[element].append((i, j))
    vecinski, _ = max(pojavitve.items(), key=lambda par: len(par[1]))
    del pojavitve[vecinski]
    izjeme = {
        mesto: vrednost
        for vrednost, mesta in pojavitve.items()
        for mesto in mesta
    }
    return (st_vrstic, st_stolpcev, vecinski, izjeme)
