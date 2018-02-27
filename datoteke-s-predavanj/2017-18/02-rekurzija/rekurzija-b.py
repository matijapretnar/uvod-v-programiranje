def fakulteta(n):
    # print('Računam fakulteto števila', n)
    if n <= 1:
        # print('To pa znam, to je kar 1!')
        return 1
    else:
        # print('Aha, moram vprašati, koliko je fakulteta števila', n - 1)
        fakulteta_prejsnjega = fakulteta(n - 1)
        # print('Sedaj pa', fakulteta_prejsnjega, 'še zmnožim z', n)
        return n * fakulteta_prejsnjega


def pocasni_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return pocasni_fibonacci(n - 1) + pocasni_fibonacci(n - 2)



def posploseni_fibonacci(a, b, n):
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return posploseni_fibonacci(b, a + b, n - 1)

def fibonacci(n):
    return posploseni_fibonacci(0, 1, n)


def stevilo_samoglasnikov(niz):
    if niz == '':
        return 0
    elif niz[0] in 'aeiouAEIOU':
        return 1 + stevilo_samoglasnikov(niz[1:])
    else:
        return stevilo_samoglasnikov(niz[1:])


def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m % n)

# oornroo

# konjak

def najdaljsi_podpalindrom(niz):
    if len(niz) <= 1:
        return niz
    elif niz[0] == niz[-1]:
        return niz[0] + najdaljsi_podpalindrom(niz[1:-1]) + niz[-1]
    else:
        brez_prve = najdaljsi_podpalindrom(niz[1:])
        brez_zadnje = najdaljsi_podpalindrom(niz[:-1])
        if len(brez_prve) > len(brez_zadnje):
            return brez_prve
        else:
            return brez_zadnje


def stevilo_stolpov(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        na_dnu_enka = stevilo_stolpov(n - 1)
        na_dnu_dvojka = stevilo_stolpov(n - 2)
        na_dnu_trojka = stevilo_stolpov(n - 3)
        return na_dnu_enka + na_dnu_dvojka + na_dnu_trojka


def stevilo_izmenjujocih_stolpov(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        na_dnu_rdeca_1 = stevilo_izmenjujocih_stolpov(n - 1)
        na_dnu_rdeca_2 = stevilo_izmenjujocih_stolpov(n - 2)
        na_dnu_modra_2 = stevilo_izmenjujocih_stolpov(n - 2)
        na_dnu_modra_3 = stevilo_izmenjujocih_stolpov(n - 3)
        return na_dnu_rdeca_1 + na_dnu_rdeca_2 + na_dnu_modra_2 + na_dnu_modra_3
