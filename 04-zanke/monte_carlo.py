import random

def oceni_pi(n):
    v_krogu = 0
    for i in range(1, n + 1):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x ** 2 + y ** 2 <= 1:
            v_krogu += 1
        print(4 * v_krogu / i)
    delez_v_krogu = v_krogu / n
    return 4 * delez_v_krogu

def nakljucna_tocka_v_krogu(x0=0, y0=0, r=1):
    while True:
        x = random.uniform(x0 - r, x0 + r)
        y = random.uniform(y0 - r, y0 + r)
        if (x - x0) ** 2 + (y - y0) ** 2 <= r ** 2:
            return x, y

def nesmiselna_naloga(st_poskusov):
    razdalja_manj_kot_pol = 0
    for _ in range(st_poskusov):
        x1, y1 = nakljucna_tocka_v_krogu()
        x2, y2 = nakljucna_tocka_v_krogu()
        if (x2 - x1) ** 2 + (y2 - y1) ** 2 <= (1 / 2) ** 2:
            razdalja_manj_kot_pol += 1
    return razdalja_manj_kot_pol / st_poskusov
