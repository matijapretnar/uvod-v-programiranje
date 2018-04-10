import os

def prestej_vrstice(ime_datoteke):
    stevec = 0
    with open(ime_datoteke) as datoteka:
        for vrstica in datoteka:
            stevec += 1
    return stevec

def prestej_znake(ime_datoteke):
    stevec = 0
    with open(ime_datoteke) as datoteka:
        for vrstica in datoteka:
            stevec += len(vrstica)
    return stevec

def prestej_pojavitve_besed(ime_datoteke):
    pojavitve = {}
    with open(ime_datoteke) as datoteka:
        for vrstica in datoteka:
            for beseda in vrstica.split():
                pojavitve[beseda] = pojavitve.get(beseda, 0) + 1
    return pojavitve

def ostevilci_vrstice(pot_vhodne, kodna_tabela='utf-8'):
    mapa_vhodne, ime_vhodne = os.path.split(os.path.abspath(pot_vhodne))
    pot_izhodne = os.path.join(mapa_vhodne, 'ostevilcena-' + ime_vhodne)
    kwargs = {
        'encoding': kodna_tabela
    }
    with open(pot_vhodne, **kwargs) as vhodna,\
         open(pot_izhodne, 'w', **kwargs) as izhodna:
        for stevilka_vrstice, vrstica in enumerate(vhodna, 1):
            print(stevilka_vrstice, vrstica, file=izhodna, end='')

# print(prestej_vrstice('martin-krpan.txt'))
# print(prestej_znake('martin-krpan.txt'))
# pojavitve_martin_krpan = prestej_pojavitve_besed('martin-krpan.txt')
# print(sorted(pojavitve_martin_krpan, key=lambda beseda: pojavitve_martin_krpan[beseda]))
# print(prestej_znake('hlapec-jernej.txt'))
# print(prestej_znake('gorjanci.txt'))
ostevilci_vrstice('martin-krpan.txt')
ostevilci_vrstice('../06-slovarji/memoizacija-b.py')