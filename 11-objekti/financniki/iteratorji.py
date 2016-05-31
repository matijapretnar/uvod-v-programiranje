class Fibonacci:
    def __init__(self):
        self.trenutni = 0
        self.naslednji = 1

    def __iter__(self):
        return self

    def __next__(self):
        prejsnji_trenutni = self.trenutni
        prejsnji_naslednji = self.naslednji
        self.trenutni = prejsnji_naslednji
        self.naslednji = prejsnji_trenutni + prejsnji_naslednji
        return prejsnji_trenutni


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


def natisni_vsa_fibonaccijeva():
    a, b = 0, 1
    while True:
        print(a)
        a, b = b, a + b


def vsa_fibonaccijeva():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def funkcija_vsa_fibonaccijeva():
    a, b = 0, 1
    while True:
        return a
        a, b = b, a + b

def enostavni_generator():
    yield 1
    yield 2
    yield 10
    yield 5
