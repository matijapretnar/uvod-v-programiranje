def gcd(m, n):
    '''Izračuna največji skupni delitelj števil m in n.'''
    if n == 0:
        return m
    else:
        ostanek = m % n
        return gcd(n, ostanek)
