from re import I


def izpisuj_zvezdice_v_nedogled(sirina=20):
    while True:
        i = 0
        while i < sirina:
            print(i * '*')
            i = i + 1
        while i > 0:
            print(i * '*')
            i = i - 1
    print(f'Končal sem pri {i}')


def izpisi_trikotnik_zvezdic(sirina=20):
    for i in range(1, sirina + 1):
        print(i * '*', i)
    for i in range(sirina - 1, 0, -1):
        print(i * '*', i)


