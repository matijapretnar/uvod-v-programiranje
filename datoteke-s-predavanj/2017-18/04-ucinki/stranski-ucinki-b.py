import turtle

def f(x):
    return x + 1

def g(x):
    print(x + 1)
    return 0

def pozdrav(ime):
    '''Vrne vljuden pozdrav za človeka z danim imenom.

    >>> pozdrav('Matija')
    'Dober dan, gospod profesor.'
    >>> pozdrav('Niels')
    'Živjo, gospod asistent.'
    >>> pozdrav('Francelj')
    'Živjo, Francelj!'
    '''
    if ime == 'Matija':
        return 'Dober dan, gospod profesor.'
    elif ime == 'Niels' or ime == 'Matjaž' or ime == 'Urban' or ime == 'Janez':
        return 'Živjo, gospod asistent.'
    elif ime == 'Jakob':
        return 'Pozdravljen, tutor!'
    else:
        return 'Živjo, ' + ime + '!'

def pozdravi():
    '''Vljudno vpraša za ime in vljudno pozdravi.'''
    ime = input('Kako ti je ime? ')
    print(pozdrav(ime))

def koch(n, d=200):
    if n == 0:
        turtle.forward(d)
    else:
        koch(n - 1, d / 3)
        turtle.left(60)
        koch(n - 1, d / 3)
        turtle.right(120)
        koch(n - 1, d / 3)
        turtle.left(60)
        koch(n - 1, d / 3)
