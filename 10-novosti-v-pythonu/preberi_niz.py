def preberi_neprazen_niz(sporocilo):
    niz = ""
    while not niz.strip():
        niz = input(sporocilo)
    return niz.strip()

def preberi_neprazen_niz(sporocilo):
    while True:
        niz = input(sporocilo)
        if niz.strip():
            return niz.strip()

def preberi_neprazen_niz(sporocilo):
    while not (niz := input(sporocilo).strip()):
        pass
    return niz

def pozdravi():
    ime = preberi_neprazen_niz("Kako ti je ime? ")
    print(f"Pozdravljen, {ime}")
