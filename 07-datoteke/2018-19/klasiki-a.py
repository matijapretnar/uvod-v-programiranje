def stevilo_vrstic(ime_datoteke):
    with open(ime_datoteke) as datoteka:
        vrstice = 0
        for vrstica in datoteka:
            vrstice += 1
        return vrstice

def stevilo_besed(ime_datoteke):
    with open(ime_datoteke) as datoteka:
        besede = 0
        for vrstica in datoteka:
            for beseda in vrstica.split():
                besede += 1
        return besede

def stevilo_znakov(ime_datoteke):
    with open(ime_datoteke) as datoteka:
        znaki = 0
        for vrstica in datoteka:
            for znak in vrstica:
                znaki += 1
        return znaki

def stevilo_koristnih_znakov(ime_datoteke):
    with open(ime_datoteke) as datoteka:
        znaki = 0
        for vrstica in datoteka:
            for znak in vrstica:
                if not znak.isspace():
                    znaki += 1
        return znaki

def povprecna_dolzina_besede(ime_datoteke):
    besede = stevilo_besed(ime_datoteke)
    znaki = stevilo_koristnih_znakov(ime_datoteke)
    return znaki / besede

def ostevilci(ime_datoteke, kodna_tabela='utf-8'):
    with open(ime_datoteke, encoding=kodna_tabela) as vhodna:
        with open('ostevilcena-' + ime_datoteke, 'w', encoding='utf-8') as izhodna:
            print('Število vrstic:', stevilo_vrstic(ime_datoteke), file=izhodna)
            print('Povprečna dolžina:', povprecna_dolzina_besede(ime_datoteke), file=izhodna)
            st_vrstice = 1
            for vrstica in vhodna:
                print(st_vrstice, vrstica, end='', file=izhodna)
                st_vrstice += 1


print(stevilo_vrstic('martin-krpan.txt'))
print(stevilo_besed('martin-krpan.txt'))
print(stevilo_znakov('martin-krpan.txt'))
print(stevilo_koristnih_znakov('martin-krpan.txt'))
print(povprecna_dolzina_besede('martin-krpan.txt'))
print(povprecna_dolzina_besede('hlapec-jernej.txt'))
# print(povprecna_dolzina_besede('gorjanci.txt'))

ostevilci('martin-krpan.txt')
ostevilci('hlapec-jernej.txt')
# ostevilci('gorjanci.txt', kodna_tabela='cp1250')
