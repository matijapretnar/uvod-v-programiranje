matrika = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

seznam = [1, 10, 20, 40]

vsota = 0
for x in seznam:
    print('začenjam obhod')
    print(x, vsota)
    vsota = vsota + x
    print('končal sem obhod')
print(vsota)

def vsota_seznama(sez):
    vsota = 0
    for element in sez:
        vsota += element
    return vsota

def dolzina_seznama(sez):
    dolzina = 0
    for element in sez:
        dolzina += 1
    return dolzina

def vsota_matrike(mat):
    vsota = 0
    print('začenjam seštevati matriko')
    for vrstica in mat:
        print('prištel bom elemente vrstice', vrstica)
        for element in vrstica:
            print('prištevam element', element)
            vsota += element
            print('zdaj je vsota', vsota)
        print('prištel sem vse elemente vrstice')
    print('prištel sem vse vrstice')
    return vsota

def sled_matrike(mat):
    sled = 0
    for i in range(len(mat)):
        sled += mat[i][i]
    return sled

    
