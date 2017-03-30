def gcd(m, n):
    '''Vrne največji skupni delitelj števil m in n.'''
    if n == 0:
        return m
    else:
        return gcd(n, m % n)