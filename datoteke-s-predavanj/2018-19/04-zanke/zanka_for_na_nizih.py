# for x in range(5):
#     print('Povedal bom, koliko je kvadrat števila', x)
#     print('Odgovor je', x ** 2)

def stevilo_samoglasnikov(niz):
    stevec = 0
    for znak in niz:
        if znak in 'aeiouAEIOU':
            stevec += 1
    return stevec

def stevilo_besed(niz):
    stevec = 0
    for beseda in niz:
        stevec += 1
    return stevec

stevilo_samoglasnikov('UVP je zakon!!!')
stevilo_besed('UVP je zakon!!!')
