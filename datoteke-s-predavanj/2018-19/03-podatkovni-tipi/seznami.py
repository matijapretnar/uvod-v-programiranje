def boljsi_pozdrav(ime):
    '''Vrne niz z ustreznim pozdravom osebe.'''
    if ime == 'Matija':
        return 'Dober dan, gospod profesor.'
    elif ime in ['Alen', 'Aljaž', 'Matjaž', 'Žiga']:
        return 'Pozdravljeni, gospod asistent.'
    elif ime == 'Anja':
        return 'Pozdravljeni, gospa asistentka.'
    else:
        return 'Živjo, ' + ime + '!'

def povprecje(seznam):
    if seznam == []:
        return  # to je isto kot return None
    else:
        return sum(seznam) / len(seznam)

def vsota_elementov(seznam):
    if seznam == []:
        return 0
    else:
        return seznam[0] + vsota_elementov(seznam[1:])
