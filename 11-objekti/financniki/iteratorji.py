class Fibonacci:
    def __init__(self):
        self.trenutni = 0
        self.naslednji = 1

    def __next__(self):
        prejsnji_trenutni = self.trenutni
        prejsnji_naslednji = self.naslednji
        self.trenutni = prejsnji_naslednji
        self.naslednji = prejsnji_trenutni + prejsnji_naslednji
        return prejsnji_trenutni