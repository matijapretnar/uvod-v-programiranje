def stevilo_vrstic(ime_datoteke):
    with open(ime_datoteke) as datoteka:
        return datoteka.read().count('\n') + 1

def stevilo_besed(ime_datoteke):
    with open(ime_datoteke) as datoteka:
        return len(datoteka.read().split())

def stevilo_znakov(ime_datoteke):
    with open(ime_datoteke) as datoteka:
        return len(datoteka.read())

def stevilo_koristnih_znakov(ime_datoteke):
    with open(ime_datoteke) as datoteka:
        return len(''.join(datoteka.read().split()))

def povprecna_dolzina_besede(ime_datoteke):
    besede = stevilo_besed(ime_datoteke)
    znaki = stevilo_koristnih_znakov(ime_datoteke)
    return znaki / besede

# def ostevilci(ime_datoteke, kodna_tabela='utf-8'):
#     with open(ime_datoteke, encoding=kodna_tabela) as vhodna:
#         with open('ostevilcena-' + ime_datoteke, 'w', encoding='utf-8') as izhodna:
#             print('Število vrstic:', stevilo_vrstic(ime_datoteke), file=izhodna)
#             print('Povprečna dolžina:', povprecna_dolzina_besede(ime_datoteke), file=izhodna)
#             st_vrstice = 1
#             for vrstica in vhodna:
#                 print(st_vrstice, vrstica, end='', file=izhodna)
#                 st_vrstice += 1


print(stevilo_vrstic('martin-krpan.txt'))
print(stevilo_besed('martin-krpan.txt'))
print(stevilo_znakov('martin-krpan.txt'))
print(stevilo_koristnih_znakov('martin-krpan.txt'))
print(povprecna_dolzina_besede('martin-krpan.txt'))
print(povprecna_dolzina_besede('hlapec-jernej.txt'))

import random

def besede_v_datoteki(ime_datoteke):
    with open(ime_datoteke) as datoteka:
        return {koren_besede(beseda) for beseda in datoteka.read().split()}

def koren_besede(beseda):
    crke = ''.join(znak for znak in beseda if znak.isalpha())
    return crke.lower().rstrip('aeiou')

def zgeneriraj_klasika(izvirnik, dolzina=200):
    besede = izvirnik.split()
    naslednje_besede = {}
    for i in range(len(besede) - 1):
        prva, druga = besede[i], besede[i + 1]
        if prva in naslednje_besede:
            naslednje_besede[prva].append(druga)
        else:
            naslednje_besede[prva] = [druga]
    nove_besede = [besede[0]]
    for _ in range(dolzina):
        nove_besede.append(random.choice(naslednje_besede[nove_besede[-1]]))
    return ' '.join(nove_besede)

with open('hlapec-jernej.txt') as datoteka:
    vsebina = datoteka.read()
    nov_boljsi_hlapec_jernej = zgeneriraj_klasika(vsebina)
    print(nov_boljsi_hlapec_jernej)

# print(besede_v_datoteki('martin-krpan.txt') & besede_v_datoteki('hlapec-jernej.txt'))
