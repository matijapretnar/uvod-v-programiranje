def memoiziraj(neumni_f):
    rezultati = {}
    def pametni_f(x):
        if x not in rezultati:
            rezultati[x] = neumni_f(x)
        return rezultati[x]
    return pametni_f

def neumni_kvadrat(x):
    print('Računam', x)
    return x ** 2

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

