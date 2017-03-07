def fibonacci(n):
    '''Vrne n-ti člen zaporedja 1, 1, 2, 3, 5, 8, ...'''
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def splosni_fibonacci(n, a, b):
    '''Vrne n-ti člen zaporedja a, b, a + b, a + 2b, 2a + 3b, ...'''
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return splosni_fibonacci(n - 1, b, a + b)

def vsota_stevil(n):
    '''Vrne vsoto števil 1 + 2 + ... + n.'''
    if n == 0:
        return 0
    return vsota_stevil(n - 1) + n

def vsota_stevil(n):
    '''Vrne vsoto števil 1 + 2 + ... + n.'''
    if n == 0:
        return 0
    else:
        return vsota_stevil(n - 1) + n

def gcd(m, n):
    '''Poišče največji skupni delitelj števil m in n.'''
    if n == 0:
        return m
    else:
        return gcd(n, m % n)


def poisci_kvadratni_koren(n, a, b, eps):
    '''Na eps natančno poišče kvadratni koren števila n na intervalu [a, b].'''
    if eps > b - a:
        return (a + b) / 2
    else:
        c = (a + b) / 2
        if c ** 2 < n:
            return poisci_kvadratni_koren(n, c, b, eps)
        else:
            return poisci_kvadratni_koren(n, a, c, eps)

def poisci_koren(n, k, a, b, eps):
    '''Na eps natančno poišče k-ti koren števila n na intervalu [a, b].'''
    if eps > b - a:
        return (a + b) / 2
    else:
        c = (a + b) / 2
        if c ** k < n:
            return poisci_koren(n, k, c, b, eps)
        else:
            return poisci_koren(n, k, a, c, eps)


def poisci_niclo(f, a, b, eps):
    '''Na eps natančno poišče ničlo funkcije f na intervalu [a, b].'''
    if eps > b - a:
        return (a + b) / 2
    else:
        c = (a + b) / 2
        if f(a) * f(c) > 0:
            return poisci_niclo(f, c, b, eps)
        else:
            return poisci_niclo(f, a, c, eps)
