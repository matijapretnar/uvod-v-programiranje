import math


def gcd(m, n):
    while n:
        m, n = n, m % n
    return m

def gcd(m, n):
    while n != 0:
        m, n = n, m % n
    return m

def gcd(m, n):
    while n != 0:
        o = m % n
        m = n
        n = o
    return m

gcd(42, 15)

# m    n     o
# 42   15    ?
#            12
# 15
#      12
#            3
# 12
#      3
#            0
# 3
#      0


def je_podniz(podniz, niz: str):
    """Vrne True natanko tedaj, kadar se podniz pojavi v nizu (ne nujno strnjeno)"""
    start = 0
    for znak in podniz:
        indeks = niz.find(znak, start)
        if indeks == -1:
            return False
        else:
            start = indeks + 1
    return True
