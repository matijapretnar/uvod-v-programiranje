import random


def posteni_kovanec():
    return random.choice(['cifra', 'grb'])

def neposteni_kovanec(verjetnost_grba):
    if random.random() < verjetnost_grba:
        return 'grb'
    else:
        return 'cifra'

def oceni_pi(stevilo_poskusov):
    v_krogu = 0
    poskusov_do_zdaj = 0
    for i in range(stevilo_poskusov):
        x = random.random()
        y = random.random()
        if x ** 2 + y ** 2 <= 1:
            v_krogu += 1
        poskusov_do_zdaj += 1
#        if i % 10000 == 0:
#            print(i, 4 * v_krogu / poskusov_do_zdaj)
    return 4 * v_krogu / stevilo_poskusov
