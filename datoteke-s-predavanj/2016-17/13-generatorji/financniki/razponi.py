def razpon_s_seznami(m, n):
    '''Vrne seznam vseh števil od m do nevključno n.'''
    razpon = []
    while m < n:
        razpon.append(m)
        m += 1
    return razpon

def razpon_z_generatorji(m, n):
    while m < n:
        yield m
        m += 1


def vsota_razpona_slaba(m, n):
    razpon = razpon_s_seznami(m, n)
    vsota = 0
    for x in razpon:
        vsota += x
    return vsota


def vsota_razpona(m, n):
    vsota = 0
    for x in razpon_z_generatorji(m, n):
        vsota += x
    return vsota


def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


def vsota_fibonaccijevih():
    vsota = 0
    for x in fibonacci():
        vsota += x
    return vsota
