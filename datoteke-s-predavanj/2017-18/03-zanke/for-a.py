def fibonacci(n):
    a = 0
    b = 1
    for m in range(n):
        a, b = b, a + b
        print(m, a, b)
    return a


for i in range(1, 11):
    print('kvadrat števila', i, 'je', i ** 2)


def stevilo_samoglasnikov_rek(niz):
    samoglasniki = 'aeiouAEIOU'
    if niz == '':
        return 0
    else:
        samoglasniki_v_preostanku = stevilo_samoglasnikov_rek(niz[1:])
        if niz[0] in samoglasniki:
            return 1 + samoglasniki_v_preostanku
        else:
            return samoglasniki_v_preostanku


def stevilo_samoglasnikov(niz):
    samoglasniki = 'aeiouAEIOU'
    stevec_samoglasnikov = 0
    for znak in niz:
        if znak in samoglasniki:
            stevec_samoglasnikov += 1
        print(znak, stevec_samoglasnikov)
    return stevec_samoglasnikov


def brez_samoglasnikov(niz):
    samoglasniki = 'aeiouAEIOU'
    soglasniki = ''
    for znak in niz:
        if znak not in samoglasniki:
            soglasniki += znak
        print(znak, soglasniki)
    return soglasniki
