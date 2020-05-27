class Zival:
    def __init__(self):
        self.starost = 0

class Pes(Zival):
    def __init__(self):
        super().__init__()
        self.veselje = 10


class Slovar:
    def __init__(self, velikost):
        self.zasedeni = 0
        self.prostori = velikost * [None]

    def _mesta_za_kljuc(self, kljuc):
        mesto = kljuc
        # Več kot toliko korakov ne bomo naredili, ker ni prostih prostorov.
        for korak in range(1, len(self.prostori) + 1):
            yield mesto % len(self.prostori)
            mesto += korak ** 2

    def _poisci_za_pisanje(self, kljuc):
        for mesto in self._mesta_za_kljuc(kljuc):
            if self.prostori[mesto] is None or self.prostori[mesto][0] == kljuc:
                return mesto

    def _poisci_za_branje(self, kljuc):
        for mesto in self._mesta_za_kljuc(kljuc):
            if self.prostori[mesto] is None:
                return
            elif self.prostori[mesto][0] == kljuc:
                return mesto

    def _razsiri(self):
        stari_prostori = self.prostori
        velikost = len(stari_prostori)
        print(f'Razširjam tabelo z {velikost} na {2 * velikost}')
        self.prostori = 2 * velikost * [None]
        for par in stari_prostori:
            if par is not None:
                kljuc, vrednost = par
                self[kljuc] = vrednost

    def __setitem__(self, kljuc, vrednost):
        mesto = self._poisci_za_pisanje(kljuc)
        self.prostori[mesto] = (kljuc, vrednost)
        self.zasedeni += 1
        if self.zasedeni > 2 * len(self.prostori) / 3:
            self._razsiri()

    def __getitem__(self, kljuc):
        mesto = self._poisci_za_branje(kljuc)
        if mesto is None:
            return
        else:
            _, vrednost = self.prostori[mesto]
            return vrednost
    
    def __contains__(self, kljuc):
        return self._poisci_za_branje(kljuc) is not None
    
    def __setattr__(self, ime_atributa, nova_vrednost):
        if ime_atributa not in ['prostori', 'zasedeni']:
            print(f'Ne pustim nastaviti {ime_atributa} na {nova_vrednost}')
        else:
            super().__setattr__(ime_atributa, nova_vrednost)
    
    def items(self):
        for x in self.prostori:
            if x is not None:
                yield x
    
    def __iter__(self):
        for x in self.prostori:
            if x is not None:
                yield x[0]

    def __eq__(self, other):
        if self.zasedeni != other.zasedeni:
            return False
        for k, v in self.items():
            if other[k] != v:
                print(k, v, other[k])
                return False
        return True

t = Slovar(5)
for i in range(1, 20, 3):
    t[i] = 10 * i
