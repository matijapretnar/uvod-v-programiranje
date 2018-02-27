def pozdrav(ime):
    if ime == 'Matija':
        return 'Dober dan, gospod profesor.'
    elif ime == 'Matjaž' or ime == 'Žiga' or ime == 'Jure' or ime == 'Janoš' or ime == 'Niels':
        return 'Pozdravljeni, gospod asistent.'
    else:
        return 'Živjo, ' + ime + '!'

def f(x):
    return 10 * x

def g(x):
    print(10 * x)
