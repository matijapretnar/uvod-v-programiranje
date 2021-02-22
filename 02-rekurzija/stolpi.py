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

def stevilo_modrih(n):
    """Vrne število stolpov, ki imajo na dnu modro kocko.
    
    >>> stevilo_modrih(3)
    2
    """
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        spodaj_modra_2 = stevilo_rdecih(n - 2)
        spodaj_modra_3 = stevilo_rdecih(n - 3)
        return spodaj_modra_2 + spodaj_modra_3

def stevilo_rdecih(n):
    """Vrne število stolpov, ki imajo na dnu rdečo kocko.
    
    >>> stevilo_rdecih(3)
    1
    """
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        spodaj_rdeca_1 = stevilo_modrih(n - 1)
        spodaj_rdeca_2 = stevilo_modrih(n - 2)
        return spodaj_rdeca_1 + spodaj_rdeca_2

def stevilo_izmenjujocih(n):
    if n == 0:
        return 1
    else:
        return stevilo_modrih(n) + stevilo_rdecih(n)
