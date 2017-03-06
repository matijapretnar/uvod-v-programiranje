def fakulteta(n):
    '''Vrne fakulteto števila n.'''
    assert n >= 0

    if n == 0:
        return 1
    else:
        return n * fakulteta(n - 1)


def fibonacci(n):
    '''Vrne n-ti člen Fibonaccijevega zaporedja 0, 1, 1, 2, 3, 5, 8…'''
    assert n >= 0
    if n == 0:
        odgovor = 0
    elif n == 1:
        odgovor = 1
    else:
        odgovor = fibonacci(n - 1) + fibonacci(n - 2)
    return odgovor

