def ponovi(f, zacetek, konec, korak):
    """Pokliče f(zacetek), f(zacetek + korak), ..., f(konec)"""
    if zacetek <= konec:
        f(zacetek)
        ponovi(f, zacetek + korak, konec, korak)

def izpisi_znak(f, x, y, dx, dy):
    #  ▘▝▀
    # ▖▌▞▛
    # ▗▚▐▜
    # ▄▙▟█"
    # zl zd sl sd
    #  0  0  0  0 - " " - 0
    #  1  0  0  0 - "▘" - 1
    #  0  1  0  0 - "▝" - 2
    #  1  1  0  0 - "▀" - 3
    #  0  0  1  0 - "▖" - 4
    #  1  0  1  0 - "▌" - 5
    #  0  1  1  0 - "▞" - 6
    #  1  1  1  0 - "▛" - 7
    zl = abs(f(x - dx / 2, y - dy / 2)) < 0.2
    zd = abs(f(x + dx / 2, y - dy / 2)) < 0.2
    sl = abs(f(x - dx / 2, y + dy / 2)) < 0.2
    sd = abs(f(x + dx / 2, y + dy / 2)) < 0.2
    indeks = int(zl) + 2 * int(zd) + 4 * int(sl) + 8 * int(sd)
    znak = ' ▘▝▀▖▌▞▛▗▚▐▜▄▙▟█'[indeks]
    print(znak, end='')

def izpisi_vrstico(f, x_min, x_max, y, dy, n_stolpcev):
    dx = (x_max - x_min) / n_stolpcev
    ponovi(
        lambda x: izpisi_znak(f, x, y, dx, dy),
        x_min,
        x_max,
        dx
    )
    print()

def implicitni_graf(f, x_min, x_max, y_min, y_max, n_vrstic, n_stolpcev):
    dy = (y_max - y_min) / n_vrstic
    ponovi(
        lambda y: izpisi_vrstico(f, x_min, x_max, y, dy, n_stolpcev),
        y_min,
        y_max,
        dy
    )

implicitni_graf(lambda x, y: x ** 2 + y ** 2 - 1, -1, 1, -1, 1, 20, 30)
import math
implicitni_graf(
    lambda x, y: math.sin(x + y) - math.cos(x * y) + 1,
    -5, 5, -5, 5, 20, 30)
implicitni_graf(
    lambda x, y: (x ** 2 + y ** 2) ** 2 - 2 * (x ** 2 - y ** 2),
    -3, 3, -1, 1, 20, 30)
# implicitni_graf(
#     lambda x, y: x - y,
#     -3, 3, -1, 1, 20, 30)
