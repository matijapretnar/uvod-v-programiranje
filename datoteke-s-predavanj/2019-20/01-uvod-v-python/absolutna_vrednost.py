def absolutna_vrednost(x):
    if x >= 0:
        return x
    else:
        return -x

def predznak(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1

def ena_funkcija(x):
    if x > 10:
        y = 5
    elif x > 0:
        y = 6
    else:
        y = 7
    return y

def druga_funkcija(x):
    if x > 10:
        y = 5
    if x > 0:
        y = 6
    else:
        y = 7
    return y
