def fakulteta(n):
    produkt = 1
    for i in range(1, n + 1):
        print(i, produkt, produkt * i)
        produkt *= i
    return produkt

def je_samoglasnik(znak):
    return znak in 'aåáeéiouAEIOU'

def stevilo_samoglasnikov(niz):
    stevec_samoglasnikov = 0
    for znak in niz:
        if je_samoglasnik(znak):
            stevec_samoglasnikov += 1
    return stevec_samoglasnikov

def brez_samoglasnikov(niz):
    nesamoglasniki = ''
    for znak in niz:
        if not je_samoglasnik(znak):
            nesamoglasniki += znak
    return nesamoglasniki
