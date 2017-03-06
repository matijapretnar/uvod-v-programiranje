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

def slovar_sosednosti(besede):
    sosednost = {}
    for i in range(len(besede) - 1):
        prva, druga = besede[i], besede[i + 1]
        if prva not in sosednost:
            sosednost[prva] = {}
        sosednost[prva][druga] = sosednost[prva].get(druga, 0) + 1
    return sosednost

def nakljucni_stavek(besede, dolzina):
    beseda = nakljucno_izberi(prestej_besede(besede))
    sosede = slovar_sosednosti(besede)
    stavek = [beseda]
    for _ in range(dolzina - 1):
        sosede_besede = sosede[beseda]
        beseda = nakljucno_izberi(sosede_besede)
        stavek.append(beseda)
    return ' '.join(stavek)

nakljucni_stavek(cankarjeve_besede, 30)
