import random

with open('../../09-datoteke/klasiki/hlapec-jernej.txt') as f:
    cankarjeve_besede = f.read().split()


def prestej_besede(besede):
    pojavitve = {}
    for beseda in besede:
        if beseda in pojavitve:
            pojavitve[beseda] += 1
        else:
            pojavitve[beseda] = 1
    return pojavitve


def nakljucno_izberi(slovar):
    moznosti = sum(slovar.values())
    izbira = random.randint(1, moznosti)
    stevec = 0
    for kljuc, vrednost in slovar.items():
        stevec += vrednost
        if stevec >= izbira:
            return kljuc

