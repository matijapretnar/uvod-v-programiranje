def fakulteta(n):
    '''Vrne fakulteto števila n.'''
    if n == 0:
        return 1
    else:
        return n * fakulteta(n - 1)

def fibonacci(n):
    '''Vrne n-to Fibonaccijevo število.'''
    assert n >= 0
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
