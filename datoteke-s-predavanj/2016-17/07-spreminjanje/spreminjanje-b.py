def stevilo_sodih_elementov(seznam):
    stevilo = 0
    for element in seznam:
        if element % 2 == 0:
            stevilo += 1
    return stevilo

def podseznam_sodih_elementov(seznam):
    podseznam = []
    for element in seznam:
        if element % 2 == 0:
            podseznam.append(element)
    return podseznam

def podseznam_kvadratov_sodih_elementov(seznam):
    podseznam = []
    for element in seznam:
        if element % 2 == 0:
            podseznam.append(element ** 2)
    return podseznam

def podseznam_kvadratov_sodih_elementov(seznam):
    return [x ** 2 for x in seznam if x % 2 == 0]

def seznam_delnih_vsot(seznam):
    delne_vsote = [seznam[0]]
    for i in range(1, len(seznam)):
        delne_vsote.append(seznam[i] + delne_vsote[-1])
    return delne_vsote

def prestej_pojavitve(seznam):
    pojavitve = {}
    for element in seznam:
        pojavitve[element] = pojavitve.get(element, 0) + 1
    return pojavitve

def zelo_pocasi_prestej_pojavitve(seznam):
    pojavitve = {}
    for element in seznam:
        pojavitve[element] = seznam.count(element)
    return pojavitve

def uredi_po_vrednostih(slovar):
    pari_vrednost_kljuc = []
    for kljuc, vrednost in slovar.items():
        pari_vrednost_kljuc.append((-vrednost, kljuc))
    urejeno_po_vrednostih = []
    for vrednost, kljuc in sorted(pari_vrednost_kljuc):
        urejeno_po_vrednostih.append((kljuc, -vrednost))
    return urejeno_po_vrednostih

def uredi_po_vrednostih2(slovar):
    pari_vrednost_kljuc = [(-vrednost, kljuc) for kljuc, vrednost in slovar.items()]
    return [(kljuc, -vrednost) for vrednost, kljuc in sorted(pari_vrednost_kljuc)]

def urejevalna_funkcija(par_kljuc_vrednost):
    kljuc, vrednost = par_kljuc_vrednost
    return (-vrednost, kljuc)

def uredi_po_vrednostih3(slovar):
    return sorted(slovar.items(), key=urejevalna_funkcija)

def uredi_po_vrednostih4(slovar):
    return sorted(slovar.items(), key=lambda par: (-par[1], par[0]))

def dolzine_elementov(seznam):
    return [len(element) for element in seznam]