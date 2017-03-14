def fibonacci(n):
    print('Računam vrednost pri', n)
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def f(x):
    return x + 2
    return x + 3
    return x + 4

def g(x):
    print(x + 2)
    print(x + 3)
    return x + 4

def pozdrav(ime):
    if ime == 'Matija':
        return 'Dober dan, gospod profesor.'
    elif ime == 'Niels' or ime == 'Urban' or ime == 'Matjaž' or ime == 'Janez':
        return 'Živjo, gospod asistent.'
    else:
        return 'Živjo, ' + ime + '!'


def pozdravi():
    ime = input('Kako ti je ime? ')
    print(pozdrav(ime))



