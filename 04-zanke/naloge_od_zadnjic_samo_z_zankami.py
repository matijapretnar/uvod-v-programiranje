def je_samoglasnik(niz):
    return len(niz) == 1 and niz.lower() in 'aeiou'


def stevilo_samoglasnikov(niz):
    samoglasniki = 0
    for crka in niz:
        if je_samoglasnik(crka):
            samoglasniki += 1
    return samoglasniki

def samoglasnike_zamenjaj_z_vprasaji(niz):
    niz_z_vprasaji = ''
    for crka in niz:
        if je_samoglasnik(crka):
            niz_z_vprasaji += '?'
        else:
            niz_z_vprasaji += crka
        print(crka, niz_z_vprasaji)
    return niz_z_vprasaji

def izpisi_kvadrat(n):
    print("┌" + (n - 2) * '-' + "┐")
    for _ in range(n - 3):
        print('|' + (n - 2) * ' ' + '|')
    print("└" + (n - 2) * '-' + "┘")

def gcd(m, n):
    while n != 0:
        o = m % n
        m = n
        n = o
        # če želite, lahko spremenljivki nastavite hkrati:
        # m, n = n, m % n
    return m
