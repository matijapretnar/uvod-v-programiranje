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
    zl = abs(f(x - dx / 2, y - dy / 2)) < 0.1
    zd = abs(f(x + dx / 2, y - dy / 2)) < 0.1
    sl = abs(f(x - dx / 2, y + dy / 2)) < 0.1
    sd = abs(f(x + dx / 2, y + dy / 2)) < 0.1
    indeks = int(zl) + 2 * int(zd) + 4 * int(sl) + 8 * int(sd)
    znak = ' ▘▝▀▖▌▞▛▗▚▐▜▄▙▟█'[indeks]
    print(znak, end='')

def implicitni_graf(f, x_min, x_max, y_min, y_max, n_vrstic, n_stolpcev):
    dx = (x_max - x_min) / n_stolpcev
    dy = (y_max - y_min) / n_vrstic
    for i in range(n_vrstic):
        for j in range(n_stolpcev):
            x = x_min + j * dx
            y = y_min + i * dy
            izpisi_znak(f, x, y, dx, dy)
        print()

def mandelbrotovo_zaporedje(c):
    z = 0
    while abs(z) < 2:
        print(z)
        z = z ** 2 + c

def ali_divergira(z, c, max_korakov=10):
    for _ in range(max_korakov):
        z = z ** 2 + c
        if abs(z) > 2:
            return False
    return True


def narisi_mandelbrotovo_mnozico(max_korakov=10, st_vrstic=80, st_stolpcev=200):
    implicitni_graf(
        lambda x, y: ali_divergira(0, x + 1j * y, max_korakov),
        -2, 2, -1, 1,
        st_vrstic, st_stolpcev
    )

def narisi_juliajevo_mnozico(max_korakov=10, st_vrstic=80, st_stolpcev=200):
    implicitni_graf(
        lambda x, y: ali_divergira(x + 1j * y, -0.73 + 0.19j, max_korakov),
        -2, 2, -1, 1,
        st_vrstic, st_stolpcev
    )

# implicitni_graf(lambda x, y: x ** 2 + y ** 2 - 1, -1, 1, -1, 1, 40, 60)

narisi_mandelbrotovo_mnozico(max_korakov=30)

# narisi_juliajevo_mnozico(max_korakov=100)
