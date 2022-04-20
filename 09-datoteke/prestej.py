with open("krst-pri-savici.txt", encoding="utf-8") as dat:
    pojavitve = {}
    for vrstica in dat:
        for beseda in vrstica.split():
            if len(beseda) >= 4:
                pojavitve[beseda] = pojavitve.get(beseda, 0) + 1

print(pojavitve)

def kljuc_najvecje_vrednosti(slovar):
    kljuc_najvecje = None
    for trenutni_kljuc in slovar:
        if kljuc_najvecje == None or slovar[trenutni_kljuc] > slovar[kljuc_najvecje]:
            kljuc_najvecje = trenutni_kljuc
    return kljuc_najvecje

print(kljuc_najvecje_vrednosti(pojavitve))