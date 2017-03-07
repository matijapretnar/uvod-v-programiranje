def pozdravi(ime):
    if ime == 'Matija':
        return 'Dober dan, gospod profesor.'
    elif ime == 'Niels' or ime == 'Urban' or ime == 'Matjaž' or ime == 'Janez':
        return 'Živjo, gospod asistent.'
    else:
        return 'Živjo, ' + ime + '!'

def dolzina_niza(niz):
    if niz == '':
        return 0
    else:
        niz_brez_glave = niz[1:]
        return 1 + dolzina_niza(niz_brez_glave)

def povprecje(seznam):
    if seznam == []:
        return None
    else:
        return sum(seznam) / len(seznam)

def dolzina_seznama(sez):
    if sez == []:
        return 0
    else:
        seznam_brez_glave = sez[1:]
        return 1 + dolzina_seznam(seznam_brez_glave)

def vsota_seznama(sez):
    if sez == []:
        return 0
    else:
        seznam_brez_glave = sez[1:]
        return sez[0] + vsota_seznama(seznam_brez_glave)
