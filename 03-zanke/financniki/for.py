produkt = 1
for k in range(1, 11):
    produkt *= k

def fakulteta(n):
    f = 1
    for k in range(1, n + 1):
        f *= k
    return f


def je_prastevilo(n):
    if n % 2 == 0:
        return n == 2
    for d in range(3, int(n ** (1 / 2)) + 2, 2):
        if n % d == 0:
            return False
    return True