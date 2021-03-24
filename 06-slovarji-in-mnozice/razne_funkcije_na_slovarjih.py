def prestej_enega(sez, x):
    pojavitve = 0
    for y in sez:
        if y == x:
            pojavitve += 1
    return pojavitve

def prestej_vse(sez):
    pojavitve = {}
    for y in sez:
        if y in pojavitve:
            pojavitve[y] += 1
        else:
            pojavitve[y] = 1
    return pojavitve

prestej_vse("lokomotiva")

def obrni_na_glavo(slovar):
    obrnjen = {}
    for k, v in slovar.items():
        if v in obrnjen:
            obrnjen[v].add(k)
        else:
            obrnjen[v] = {k}
    return obrnjen
