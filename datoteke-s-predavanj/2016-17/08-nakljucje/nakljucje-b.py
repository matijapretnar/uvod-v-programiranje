import random

def posteni_kovanec():
    return random.choice(['cifra', 'grb'])

def neposteni_kovanec(verjetnost_grba):
    if random.random() < verjetnost_grba:
        return 'grb'
    else:
        return 'cifra'

def sredine_kvadratov(x):
    dolzina = len(str(x))
    while True:
        x = x ** 2
        x //= 10 ** (dolzina // 2)
        x %= 10 ** dolzina
        yield x

def lcg(x, a=1103515245, c=12345, m=2 ** 31 - 1):
    while True:
        x = (a * x + c) % m
        yield x

generator = sredine_kvadratov(3792)

def nakljucna_stevka():
    return next(generator) % 10

def prestej_pojavitve(seznam):
    pojavitve = {}
    for element in seznam:
        pojavitve[element] = pojavitve.get(element, 0) + 1
    return pojavitve

