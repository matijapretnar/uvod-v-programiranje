def vsebina_datoteke(ime_datoteke):
    '''Vrne niz s celotno vsebino datoteke z danim imenom.'''
    with open(ime_datoteke) as f:
        return f.read()


def koren_besede(beseda):
    '''Vrne del besede pred zadnjim samoglasnikom. Če ga ni, vrne celotno besedo.'''
    for i in range(len(beseda) - 1, -1, -1):
        if beseda[i] in 'aeiou':
            return beseda[:i]
    return beseda


def pociscena_beseda(beseda):
    '''Vrne besedo brez vseh znakov, ki ne predstavljajo črk.'''
    return ''.join(znak for znak in beseda.lower() if znak.isalpha())


def prestej_korene(besedilo):
    '''Vrne slovar pojavitev vseh korenov besed v danem besedilu.'''
    pojavitve_korenov = {}
    for beseda in besedilo.split():
        beseda = pociscena_beseda(beseda)
        if len(beseda) > 2:
            koren = koren_besede(beseda)
            pojavitve_korenov[koren] = pojavitve_korenov.get(koren, 0) + 1
    return pojavitve_korenov


def najvecje_vrednosti(slovar, stevilo=50):
    '''Vrne dano število parov z največjimi vrednosti v danem slovarju.'''
    po_vrednostih = sorted(slovar.items(), key=lambda par: par[1], reverse=True)
    print(po_vrednostih[:stevilo])


def najdaljsa_beseda(besedilo):
    return max(besedilo.split(), key=len)

# najvecje_vrednosti(prestej_korene(vsebina_datoteke('gorjanci.txt')))
# print(najdaljsa_beseda(vsebina_datoteke('hlapec-jernej.txt')))


def prestej_crke(niz):
    '''Vrne slovar pojavitev črk v danem nizu.'''
    pojavitve = {}
    for znak in niz:
        if znak in pojavitve:
            pojavitve[znak] += 1
        else:
            pojavitve[znak] = 1
    return pojavitve

# def prestej_crke(niz):
#     '''Vrne slovar pojavitev črk v danem nizu.'''
#     pojavitve = {}
#     for znak in niz:
#         pojavitve[znak] = niz.count(znak)
#     return pojavitve

# print(prestej_crke(vsebina_datoteke('gorjanci.txt')))
print(prestej_crke(vsebina_datoteke('gorjanci.txt')))
