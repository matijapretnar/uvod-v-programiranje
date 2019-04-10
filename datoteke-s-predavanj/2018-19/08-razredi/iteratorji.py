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

i = IteratorCezNiz('to je en niz')

class IteratorFibonaccijevih:
    def __init__(self):
        self.a = 0
        self.b = 1
    def __next__(self):
        prejsnji_a = self.a
        prejsnji_b = self.b
        self.a = prejsnji_b
        self.b = prejsnji_a + prejsnji_b
        return prejsnji_a

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b