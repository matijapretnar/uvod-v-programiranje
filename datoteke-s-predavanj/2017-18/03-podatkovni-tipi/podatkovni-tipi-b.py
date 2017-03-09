def f(x):
    x + 2

def pozdravi(ime):
    '''Vljudno pozdravi človeka z danim imenom.

    >>> pozdravi('Matija')
    'Dober dan, gospod profesor.'
    >>> pozdravi('Niels')
    'Živjo, gospod asistent.'
    >>> pozdravi('Francelj')
    'Živjo, Francelj!'
    '''
    if ime == 'Matija':
        return 'Dober dan, gospod profesor.'
    elif ime == 'Niels' or ime == 'Matjaž' or ime == 'Urban' or ime == 'Janez':
        return 'Živjo, gospod asistent.'
    else:
        return 'Živjo, ' + ime + '!'

# Najbolj len način
dolzina1 = len


# Drugi najbolj len način
def dolzina2(niz):
    '''Vrne dolžino danega niza.'''
    return len(niz)


# Najbolj nesmiselen (in tudi precej neučinkovit) način
def dolzina3(niz):
    '''Vrne dolžino danega niza.'''
    if niz == '':
        return 0
    else:
        return 1 + dolzina3(niz[1:])

def povprecje1(sez):
    return sum(sez) / len(sez)

def povprecje2(sez):
    if sez == []:
        return None
    else:
        return sum(sez) / len(sez)

def povprecje3(sez):
    if sez:
        return sum(sez) / len(sez)
    else:
        return None

def povprecje4(sez):
    if sez:
        return sum(sez) / len(sez)

def dolzina_seznama(sez):
    if sez:
        return 1 + dolzina_seznama(sez[1:])
    else:
        return 0

def dolzina_niza(niz):
    if niz:
        return 1 + dolzina_niza(niz[1:])
    else:
        return 0

def vsota_seznama(sez):
    if sez:
        return sez[0] + vsota_seznama(sez[1:])
    else:
        return 0

def max_seznama(sez):
    if len(sez) == 1:
        return sez[0]
    elif sez:
        return max(sez[0], max_seznama(sez[1:]))

