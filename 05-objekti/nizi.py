def yoda(stavek):
    locilo = stavek[-1]
    stavek_brez_locila = stavek.replace(locilo, '')
    besede = stavek_brez_locila.split()
    zadnja_beseda = besede[-1]
    ostale_besede = besede[:-1]
    obrnjene_besede = [zadnja_beseda] + ostale_besede
    obrnjen_stavek = ' '.join(obrnjene_besede) + locilo
    return obrnjen_stavek.capitalize()

print(yoda('Jaz sem Yoda!'))
print(yoda('Kdo si ti?'))
print(yoda('UVP je zakon.'))


def izpisi_kvadrate(n):
    for i in range(1, n + 1):
        print(str(i) + '^2 = ' + str(i ** 2))
        print(i, '^2 = ', i ** 2, sep='')
        print('{stevilo}^2 = {kvadrat}'.format(stevilo=i, kvadrat=i ** 2))

izpisi_kvadrate(10)




