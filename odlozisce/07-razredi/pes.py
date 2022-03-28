class Pes:
    def __init__(self, glas='hov'):
        self.glasnost = 1
        self.glas = glas

    def kaj_zalaja(self):
        return self.glasnost * self.glas

    def daj_glas(self):
        print(self.kaj_zalaja())

    def spusti_na_sprehod(self):
        self.glasnost *= 2

    def __repr__(self):
        return f'Pes(glas={repr(self.glas)})'

    def __str__(self):
        return f'En lušten kuža, ki dela {self.kaj_zalaja()}'

    def __add__(self, other):
        otrok = Pes(glas=self.glas + other.glas)
        otrok.glasnost = (self.glasnost + other.glasnost) // 2
        return otrok

    def __len__(self):
        return 1000