def pozdrav(ime):
    '''Vrne niz z ustreznim pozdravom osebe.'''
    if ime == 'Matija':
        return 'Dober dan, gospod profesor.'
    elif ime == 'Alen' or ime == 'Aljaž' or ime == 'Matjaž' or ime == 'Žiga':
        return 'Pozdravljeni, gospod asistent.'
    elif ime == 'Anja':
        return 'Pozdravljeni, gospa asistentka.'
    else:
        return 'Živjo, ' + ime + '!'

def stevilo_samoglasnikov(niz):
    samoglasniki = 'aeiouAEIOU'
    if niz == '':
        return 0
    elif niz[0] in samoglasniki:
        # preostanek_niza = niz[1:]
        # samoglasniki_v_preostanku_niza = stevilo_samoglasnikov(preostanek_niza)
        # return 1 + samoglasniki_v_preostanku_niza
        return 1 + stevilo_samoglasnikov(niz[1:])
    else:
        return stevilo_samoglasnikov(niz[1:])

stevilo_samoglasnikov('miza')
