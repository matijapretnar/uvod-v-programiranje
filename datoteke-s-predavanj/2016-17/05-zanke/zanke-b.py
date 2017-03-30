def dolzina_seznama(seznam):
    stevilo_videnih_elementov = 0

    for _ in seznam:
        stevilo_videnih_elementov += 1

    return stevilo_videnih_elementov


def vsota_seznama(seznam):
    vsota_do_sedaj_videnih_elementov = 0

    for element in seznam:
        vsota_do_sedaj_videnih_elementov += element

    return vsota_do_sedaj_videnih_elementov


def najvecji_element(seznam):
    if seznam == []:
        return None

    najvecji_do_sedaj_videni_element = seznam[0]

    for trenutni_element in seznam:
        if trenutni_element > najvecji_do_sedaj_videni_element:
            najvecji_do_sedaj_videni_element = trenutni_element

    return najvecji_do_sedaj_videni_element


def najdaljsi_podseznam(seznam):
    if seznam == []:
        return None

    najdaljsi_do_sedaj_videni_podseznam = seznam[0]

    for trenutni_podseznam in seznam:
        print(najdaljsi_do_sedaj_videni_podseznam, trenutni_podseznam)
        if len(trenutni_podseznam) > len(najdaljsi_do_sedaj_videni_podseznam):
            najdaljsi_do_sedaj_videni_podseznam = trenutni_podseznam

    return najdaljsi_do_sedaj_videni_podseznam

def vsota_seznama_z_range(seznam):
    vsota = 0
    for i in range(len(seznam)):
        vsota += seznam[i]
    return vsota

def vsota_matrike(matrika):
    vsota = 0
    for vrstica in matrika:
        for element in vrstica:
            vsota += element
    return vsota

def vsota_matrike_z_range(matrika):
    vsota = 0
    for i in range(len(matrika)):
        for j in range(len(matrika[i])):
            vsota += matrika[i][j]
    return vsota

def sled_matrike(matrika):
    vsota = 0
    for i in range(len(matrika)):
        if i >= len(matrika[i]):
            break
        vsota += matrika[i][i]
    return vsota

def vrednost_polinoma1(koeficienti, x):
    vrednost = 0
    potenca = 0
    for koef in koeficienti:
        vrednost += koef * x ** potenca
        potenca += 1
    return vrednost

def vrednost_polinoma2(koeficienti, x):
    vrednost = 0
    for potenca in range(len(koeficienti)):
        vrednost += koeficienti[potenca] * x ** potenca
    return vrednost

def vrednost_polinoma3(koeficienti, x):
    vrednost = 0
    for potenca, koeficient in enumerate(koeficienti):
        vrednost += koef * x ** potenca
    return vrednost

def kdaj_harmonicna_preseze(x):
    vsota = 0
    n = 1
    while vsota <= x:
        vsota += 1 / n
        n += 1
    return n - 1

def moj_generator(n):
    yield n
    print('A')
    yield n
    print('B')
    yield n
    print('C')