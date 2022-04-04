def moj_range(i, j):
    k = i
    while k <= j:
        return k
        k += 1

def moj_range2(i, j):
    sez = []
    k = i
    while k <= j:
        sez.append(k)
        k += 1
    return sez

def moj_range3(i, j):
    k = i
    while k <= j:
        print(k)
        k += 1

def moj_range4(i, j):
    k = i
    while k <= j:
        yield k
        k += 1
