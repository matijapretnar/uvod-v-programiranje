def je_samoglasnik(znak):
    return znak in 'aeiou'



def prestej_samoglasnike(niz):
    stevilo_samoglasnikov = 0
    for znak in niz:
        if je_samoglasnik(znak):
            stevilo_samoglasnikov += 1
    return stevilo_samoglasnikov

prestej_samoglasnike('lokomotiva')