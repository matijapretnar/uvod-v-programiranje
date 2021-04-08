def prestej_vrstice(ime_datoteke):
    with open(ime_datoteke, encoding="UTF-8") as dat:
        st_vrstic = 0
        for _ in dat:
            st_vrstic += 1
        return st_vrstic

def prestej_znake(ime_datoteke):
    with open(ime_datoteke, encoding="UTF-8") as dat:
        st_znakov = 0
        for vrstica in dat:
            st_znakov += len(vrstica)
        return st_znakov

def prestej_besede(ime_datoteke):
    with open(ime_datoteke, encoding="UTF-8") as dat:
        st_znakov = 0
        for vrstica in dat:
            st_znakov += len(vrstica.split())
        return st_znakov

def ostevilci_vrstice(ime_vhodne, ime_izhodne):
    with open(ime_vhodne, encoding="UTF-8") as vhodna:
        with open(ime_izhodne, "w", encoding="UTF-8") as izhodna:
            for st_vrstice, vrstica in enumerate(vhodna, 1):
                # izhodna.write(str(st_vrstice) + " " + vrstica)
                izhodna.write(f"{st_vrstice} {vrstica}")
