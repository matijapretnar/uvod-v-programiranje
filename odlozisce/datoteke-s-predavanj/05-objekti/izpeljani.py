def seznam_kvadratov(seznam):
    return [x ** 2 for x in seznam]

def dolzine_besed(seznam):
    return [len(beseda) for beseda in seznam]

def delne_vsote(seznam):
    vsote = []
    vsota = 0
    for x in seznam:
        vsota += x
        vsote.append(vsota)
    return vsote

def sodi_elementi(seznam):
    return [x for x in seznam if x % 2 == 0]

def vrni_brez_pojavitev(seznam, x):
    return [y for y in seznam if x != y]

def pobrisi_vse_pojavitve(seznam, x):
    seznam[:] = vrni_brez_pojavitev(seznam, x)

def pobrisi_vse_pojavitve_pocasna(seznam, x):
    while x in seznam:
        seznam.remove(x)

def vrni_brez_pojavitev_pocasna(seznam, x):
    kopija = seznam[:]
    pobrisi_vse_pojavitve_pocasna(kopija, x)
    return kopija
