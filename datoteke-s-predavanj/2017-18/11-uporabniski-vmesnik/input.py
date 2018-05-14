def pozdrav(ime):
    if ime == 'Matija':
        return 'Dober dan, gospod profesor.'
    elif ime in ['Matjaž', 'Žiga', 'Jure', 'Janoš', 'Niels']:
        return 'Pozdravljeni, gospod asistent.'
    else:
        return 'Živjo, ' + ime + '!'

def zacni_pozdravljati():
    while True:
        ime = input('Kako ti je ime? ')
        print(pozdrav(ime))
