class Ponavljalec:
    def __init__(self, x, n):
        self.x = x
        self.n = n
    def __next__(self):
        if self.n > 0:
            self.n -= 1
            return self.x
        else:
            raise StopIteration
        
class Pes:
    def __init__(self, glas='hov', veselje=1):
        self.glas = glas
        self.veselje = veselje
    def __iter__(self):
        return Ponavljalec(f'{self.glas}!', self.veselje)
    def daj_glas(self):
        print(self.veselje * self.glas + '!')
    def razveseli(self):
        self.veselje += 1
    def __repr__(self):
        return f'Pes(glas={self.glas!r}, veselje={self.veselje})'
    def __lt__(self, other):
        return self.veselje < other.veselje

class Prazen:
    pass

fido = Pes(veselje=10)
runo = Pes(glas='vuf')