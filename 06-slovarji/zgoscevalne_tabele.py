def nova_zgoscevalna_tabela(velikost):
    return {'zasedeni': 0, 'prostori': velikost * [None]}

def poisci_za_pisanje(prostori, kljuc):
    mesto = kljuc % len(prostori)
    korak = 1
    while True:
        if prostori[mesto] is None:
            return mesto
        elif prostori[mesto][0] == kljuc:
            return mesto
        else:
            mesto = (mesto + korak ** 2) % len(prostori)
            korak += 1

def poisci_za_branje(prostori, kljuc):
    mesto = kljuc % len(prostori)
    korak = 1
    while True:
        if prostori[mesto] is None:
            return
        elif prostori[mesto][0] == kljuc:
            return mesto
        else:
            mesto = (mesto + korak ** 2) % len(prostori)
            korak += 1

def razsiri(tabela):
    stari_prostori = tabela['prostori']
    velikost = len(stari_prostori)
    print(f'Razširjam tabelo z {velikost} na {2 * velikost}')
    novi_prostori = 2 * velikost * [None]
    for par in stari_prostori:
        if par is not None:
            kljuc, vrednost = par
            mesto = poisci_za_pisanje(novi_prostori, kljuc)
            novi_prostori[mesto] = (kljuc, vrednost)
    tabela['prostori'] = novi_prostori


def dodaj(tabela, kljuc, vrednost):
    prostori = tabela['prostori']
    mesto = poisci_za_pisanje(prostori, kljuc)
    prostori[mesto] = (kljuc, vrednost)
    tabela['zasedeni'] += 1
    if tabela['zasedeni'] > 2 * len(prostori) / 3:
        razsiri(tabela)

def poisci(tabela, kljuc):
    prostori = tabela['prostori']
    mesto = poisci_za_branje(prostori, kljuc)
    if mesto is None:
        return
    else:
        _, vrednost = prostori[mesto]
        return vrednost

t = nova_zgoscevalna_tabela(5)
for i in range(1, 10000000, 7):
    dodaj(t, i, 10 * i)
