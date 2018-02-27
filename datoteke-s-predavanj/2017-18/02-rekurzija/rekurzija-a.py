def fakulteta(n):
    # print('Računam fakulteto od', n)
    if n <= 1:
        # print('Enostaven primer!')
        return 1
    else:
        # print('Aha, moram najprej izračunati fakulteto od', n - 1)
        fakulteta_prejsnjega = fakulteta(n - 1)
        # print('Rezultat je', fakulteta_prejsnjega)
        # print('Zdaj pa le še zmnožim z', n)
        return n * fakulteta_prejsnjega

def neustavljiva_fakulteta(n):
    return n * neustavljiva_fakulteta(n - 1)

def fibonacci(n):
    print('Računam fibonacci', n)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def stevilo_samoglasnikov(niz):
    samoglasniki = 'aeiouAEIOU'
    if niz == '':
        return 0
    else:
        samoglasniki_v_preostanku = stevilo_samoglasnikov(niz[1:])
        if niz[0] in samoglasniki:
            return 1 + samoglasniki_v_preostanku
        else:
            return samoglasniki_v_preostanku
