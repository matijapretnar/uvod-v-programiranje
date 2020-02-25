def stevilo_stolpov(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        spodaj_modra_1 = stevilo_stolpov(n - 1)
        spodaj_rdeca_2 = stevilo_stolpov(n - 2)
        spodaj_zelena_3 = stevilo_stolpov(n - 3)
        return spodaj_modra_1 + spodaj_rdeca_2 + spodaj_zelena_3