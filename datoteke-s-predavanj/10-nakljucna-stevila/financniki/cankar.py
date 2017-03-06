import random

def prestej_pojavitve_besed(besedilo):
    '''Vrne slovar pojavitev besed v danem besedilu.'''
    pojavitve = {}
    for beseda in besedilo.split():
        pojavitve[beseda] = pojavitve.get(beseda, 0) + 1
    return pojavitve


def izberi_kljuc(slovar_pogostosti):
    meja = random.randint(1, sum(slovar_pogostosti.values()))
    dosezeno = 0
    for kljuc, velikost in slovar_pogostosti.items():
        dosezeno += velikost
        if dosezeno >= meja:
            return kljuc


def sosednje_besede(besedilo):
    sosede = {}
    besede = besedilo.split()
    for indeks in range(len(besede) - 1):
        prva, druga = besede[indeks], besede[indeks + 1]
        if prva not in sosede:
            sosede[prva] = {}
        sosede[prva][druga] = sosede[prva].get(druga, 0) + 1
    return sosede




with open('../../09-datoteke/klasiki/hlapec-jernej.txt') as datoteka:
    cankarjeve_besede = sosednje_besede(datoteka.read())


def nakljucni_stavek(slovar_pogostosti, dolzina_stavka):
    besede = []
    for _ in range(dolzina_stavka):
        beseda = izberi_kljuc(slovar_pogostosti)
        besede.append(beseda)
    return " ".join(besede)


def pravi_nakljucni_stavek(slovar_pogostosti_po_besedah, dolzina_stavka):
    besede = []
    beseda = random.choice(list(slovar_pogostosti_po_besedah.keys()))
    for _ in range(dolzina_stavka):
        beseda = izberi_kljuc(slovar_pogostosti_po_besedah[beseda])
        besede.append(beseda)
    return " ".join(besede)