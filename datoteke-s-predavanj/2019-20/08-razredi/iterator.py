class IteratorCezNiz:
    def __init__(self, niz):
        self.niz = niz
        self.indeks = 0
    def __next__(self):
        if self.indeks < len(self.niz):
            self.indeks += 1
            return self.niz[self.indeks - 1]
        else:
            raise StopIteration


class NekajKarMiVednoDaNaslednjiZnakNiza:
    def __init__(self, niz):
        self.niz = niz
        self.indeks = 0
    def __next__(self):
        if self.indeks < len(self.niz):
            self.indeks += 1
            return self.niz[self.indeks - 1]
        else:
            return False

class IteratorFibonaccijevih:
    def __init__(self, a=0, b=1):
        self.a = a
        self.b = b
    def __next__(self):
        prejsnji_a = self.a
        prejsnji_b = self.b
        self.a = prejsnji_b
        self.b = prejsnji_a + prejsnji_b
        return prejsnji_a

nkvnksdf = NekajKarMiVednoDaNaslednjiZnakNiza('blabla')