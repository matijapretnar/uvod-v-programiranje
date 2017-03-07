def kvadratna(x):
    potenca = 2
    y = x ** potenca
    return y

def predznak1(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

def predznak2(x):
    if x > 0:
        p = 1
    elif x < 0:
        p = -1
    else:
        p = 0
    return p

def predznak3(x):
    if x > 0:
        p = 1
    if x < 0:
        p = -1
    else:
        p = 0
    return p

def je_sodo1(x):
    return x % 2 == 0

def je_sodo2(x):
    if x % 2 == 0:
        return True
    else:
        return False

def je_sodo3(x):
    if x == 0:
        return True
    elif x == 1:
        return False
    else:
        return je_sodo3(x - 2)

def je_sodo4(x):
    if x == 0:
        return True
    else:
        return je_liho4(x - 1)

def je_liho4(x):
    if x == 0:
        return False
    else:
        return je_sodo4(x - 1)


def je_sodo5(x):
    if x == 0:
        return True
    else:
        return not je_sodo5(x - 1)

def stevilo_deliteljev_vsaj(n, k):
    if k > n:
        return 0
    elif n % k == 0:
        return 1 + stevilo_deliteljev_vsaj(n, k + 1)
    else:
        return stevilo_deliteljev_vsaj(n, k + 1)

def stevilo_deliteljev(n):
    return stevilo_deliteljev_vsaj(n, 1)

def vsota_naravnih(n):
    if n == 0:
        return 0
    else:
        return n + vsota_naravnih(n - 1)
