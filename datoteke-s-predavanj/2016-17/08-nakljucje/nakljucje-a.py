import random


def posteni_kovanec():
    return random.choice(['cifra', 'grb'])

def neposteni_kovanec(verjetnost_grba):
    if random.random() < verjetnost_grba:
        return 'grb'
    else:
        return 'cifra'
