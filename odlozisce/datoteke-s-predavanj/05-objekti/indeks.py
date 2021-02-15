def indeks(iterable, x, pojavitev):
    zacetek = 0
    for st_pojavitve in range(pojavitev):
        nova_pojavitev = iterable.index(x, zacetek)
        zacetek = nova_pojavitev + 1
    return nova_pojavitev

mesto_tretje_pojavitve = indeks([1, 2, 1, 3, 1, 4, 1, 5, 1, 6], 1, 3)
1 + 1