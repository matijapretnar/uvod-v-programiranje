def koren(n):
    spodnja_meja = 0
    zgornja_meja = max(1, n)
    while zgornja_meja - spodnja_meja > 1e-10:
        sredina = (spodnja_meja + zgornja_meja) / 2
        sredina2 = sredina * sredina
        if sredina2 == n:
            return sredina
        elif sredina2 < n:
            spodnja_meja = sredina
        else:
            zgornja_meja = sredina
    return sredina

koren(3)


