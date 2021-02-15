ime_datoteke = 'martin-krpan.txt'

print('Odpiram datoteko')
with open(ime_datoteke) as datoteka:
    print('Datoteka je zdaj odprta')
    # vsebina_datoteke = datoteka.read()

    print(ime_datoteke.count('M'))
    print(ime_datoteke.count('m'))
    print(ime_datoteke.count('Martin'))
    1 / 0
    for vrstica in datoteka:
        print(vrstica.upper()[:50], '...')
    print('Datoteko bom zdaj zaprl')
print('Datoteka je zdaj zaprta')

