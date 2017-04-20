import random

def posteni_kovanec():
    return random.choice(['cifra', 'grb'])

def neposteni_kovanec(verjetnost_grba):
    if random.random() < verjetnost_grba:
        return 'grb'
    else:
        return 'cifra'

def sredine_kvadratov(x):
    dolzina = len(str(x))
    while True:
        x = x ** 2
        x //= 10 ** (dolzina // 2)
        x %= 10 ** dolzina
        yield x

def lcg(x, a=1103515245, c=12345, m=2 ** 31 - 1):
    while True:
        x = (a * x + c) % m
        yield x

generator = lcg(3792)

def nakljucna_stevka():
    return next(generator) % 10

def nakljucno_naravno_stevilo(maksi):
    najvecje_mozno_generirano = 2 ** 31 - 2
    najvecje_ki_pride_v_postev = najvecje_mozno_generirano - najvecje_mozno_generirano % maksi
    while True:
        nakljucno_stevilo = next(generator)
        if nakljucno_stevilo <= najvecje_ki_pride_v_postev:
            return nakljucno_stevilo % maksi

def nakljucno_realno_stevilo(a=0, b=1):
    return a + (b - a) * (next(generator) / (2 ** 31 - 2))

def prestej_pojavitve(seznam):
    pojavitve = {}
    for element in seznam:
        pojavitve[element] = pojavitve.get(element, 0) + 1
    return pojavitve

def oceni_pi(stevilo_poskusov):
    tocke_v_krogu, vse_tocke = 0, 0
    for _ in range(stevilo_poskusov):
        x = random.random()
        y = random.random()
        if x ** 2 + y ** 2 <= 1:
            tocke_v_krogu += 1
        vse_tocke += 1
    return 4 * tocke_v_krogu / vse_tocke

def binomski_simbol(n, k):
    if k == 0:
        return 1
    else:
        return (n - k + 1) * binomski_simbol(n, k - 1) // k    

def verjetnost_cifer(stevilo_metov, stevilo_cifer):
    return sum((
        binomski_simbol(stevilo_metov, k)
        for
        k
        in
        range(stevilo_cifer, stevilo_metov + 1)
    )) / (2 ** stevilo_metov)


def oceni_verjetnost_cifer(stevilo_metov, stevilo_cifer, stevilo_poskusov=100000):
    padlo_je_vec_kot_toliko_cifer = 0
    for _ in range(stevilo_poskusov):
        cifre = 0
        for _ in range(stevilo_metov):
            if random.random() > 1 / 2:
                cifre += 1
        if cifre >= stevilo_cifer:
            padlo_je_vec_kot_toliko_cifer += 1
    return padlo_je_vec_kot_toliko_cifer / stevilo_poskusov

