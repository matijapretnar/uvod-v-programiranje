def stevilo_vrstic(ime_datoteke, kodna_tabela='utf-8'):
    stevec = 0
    with open(ime_datoteke, encoding=kodna_tabela) as datoteka:
        for vrstica in datoteka:
            stevec += 1
    return stevec

def stevilo_znakov(ime_datoteke, kodna_tabela='utf-8'):
    stevec = 0
    with open(ime_datoteke, encoding=kodna_tabela) as datoteka:
        for vrstica in datoteka:
            stevec += len(vrstica)
    return stevec

def stevilo_besed(ime_datoteke, kodna_tabela='utf-8'):
    stevec = 0
    with open(ime_datoteke, encoding=kodna_tabela) as datoteka:
        for vrstica in datoteka:
            stevec += len(vrstica.split())
    return stevec

def ostevilci_vrstice(ime_datoteke, kodna_tabela='utf-8'):
    stevilka_vrstice = 1
    with open(ime_datoteke, encoding=kodna_tabela) as vhodna:
        with open('ostevilcena-' + ime_datoteke, 'w', encoding=kodna_tabela) as izhodna:
            for vrstica in vhodna:
                print(stevilka_vrstice, vrstica, file=izhodna)
                stevilka_vrstice += 1


print(stevilo_vrstic('martin-krpan.txt'))
print(stevilo_vrstic('../07-iteracija/generatorji-b.py'))
print(stevilo_znakov('martin-krpan.txt'))
print(stevilo_besed('martin-krpan.txt'))
print(stevilo_vrstic('hlapec-jernej.txt'))
print(stevilo_znakov('hlapec-jernej.txt'))
print(stevilo_besed('hlapec-jernej.txt'))
print(stevilo_vrstic('gorjanci.txt', kodna_tabela='cp1250'))
print(stevilo_znakov('gorjanci.txt', kodna_tabela='cp1250'))
print(stevilo_besed('gorjanci.txt', kodna_tabela='cp1250'))
ostevilci_vrstice('martin-krpan.txt')