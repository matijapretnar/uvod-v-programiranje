from preseren import krst_pri_savici

slovar = {
    'mama': 'mother',
    'je': 'is eating',
    'kosilo': 'lunch',
}

def prevedi_besedo(beseda):
    return slovar.get(beseda, beseda)

def prevedi_stavek(stavek):
    prevodi = []
    for beseda in stavek.split():
        prevodi.append(prevedi_besedo(beseda))
    return ' '.join(prevodi)

def prestej_pojavitve(itrbl):
    pojavitve = {}
    for x in itrbl:
        pojavitve[x] = pojavitve.get(x, 0) + 1
    return pojavitve


def izlusci_besede(niz, najmanjsa_dolzina=3):
    for znak in ',.!?-':
         niz = niz.replace(znak, ' ')
    besede = []
    for beseda in niz.split():
        beseda = beseda.rstrip('aeiou')
        if len(beseda) >= najmanjsa_dolzina:
            besede.append(beseda)
    return besede

print(len(krst_pri_savici))