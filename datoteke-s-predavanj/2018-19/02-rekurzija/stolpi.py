def stevilo_stolpov(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        na_vrhu_1 = stevilo_stolpov(n - 1)
        na_vrhu_2 = stevilo_stolpov(n - 2)
        na_vrhu_3 = stevilo_stolpov(n - 3)
        return na_vrhu_1 + na_vrhu_2 + na_vrhu_3

def stevilo_modrih_stolpov(n):
    '''Vrne število vseh stolpov izmenjujočih barv, ki imajo na vrhu modro kocko.'''
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        na_vrhu_modra_2 = stevilo_rdecih_stolpov(n - 2)
        na_vrhu_modra_3 = stevilo_rdecih_stolpov(n - 3)
        return na_vrhu_modra_2 + na_vrhu_modra_3

def stevilo_rdecih_stolpov(n):
    '''Vrne število vseh stolpov izmenjujočih barv, ki imajo na vrhu rdečo kocko.'''
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        na_vrhu_rdeca_1 = stevilo_modrih_stolpov(n - 1)
        na_vrhu_rdeca_2 = stevilo_modrih_stolpov(n - 2)
        return na_vrhu_rdeca_1 + na_vrhu_rdeca_2

def stevilo_pisanih_stolpov(n):
    if n == 0:
        return 1
    else:
        return stevilo_modrih_stolpov(n) + stevilo_rdecih_stolpov(n)

