def pozdrav(ime):
    if ime == 'Matija':
        return 'Dober dan, gospod profesor.'
    elif ime == 'Anja':
        return 'Pozdravljena, gospa asistentka.'
    elif ime in ['Filip', 'Matjaž', 'Aljaž']:
        return 'Pozdravljeni, gospod asistent.'
    else:
        return 'Živjo, ' + ime
