n = 2

def ponovi(f, i, j):
    if i < j:
        f(i)
        ponovi(f, i + 1, j)

def narisi_graf(f):
    ponovi(lambda i: narisi_vrstico(f, i), -n, n + 1)

def narisi_vrstico(f, i):
    ponovi(lambda j: narisi_znak(f, i, j), -n, n + 1)
    print()

def narisi_znak(f, i, j):
    d = 1 / (2 * n)
    y, x = i / n , j / n
    # print(znak1(f(x, y) < 0), end="")
    # print(znakv(f(x, y) < 0, f(x, y + d) < 0), end="")
    # print(znakh(f(x, y) < 0, f(x + d, y) < 0), end="")
    print(znakhv(f(x, y) < 0, f(x + d, y) < 0, f(x, y + d) < 0, f(x + d, y + d) < 0), end="")

def znak1(indeks):
    return " █"[indeks]

def znakv(z, s):
    indeks = z + 2 * s
    return " ▀▄█"[indeks]

def znakh(l, d):
    indeks = l + 2 * d
    return " ▌▐█"[indeks]

def znakhv(zl, zd, sl, sd):
    indeks = zl + 2 * zd + 4 * sl + 8 * sd
    return " ▘▝▀▖▌▞▛▗▚▐▜▄▙▟█"[indeks]

narisi_graf(lambda x, y: x ** 2 + y ** 2 - 1)
