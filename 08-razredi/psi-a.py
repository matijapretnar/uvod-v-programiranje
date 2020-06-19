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
    def __init__(self, glas='hov'):
        self.veselje = 1
        self.glas = glas
    
    def __repr__(self):
        return "Pes(glas={!r})".format(self.glas)
    
    def __add__(self, other):
        pol_mame = self.glas[:len(self.glas) // 2]
        pol_ata = other.glas[len(other.glas) // 2:]
        return Pes(glas=pol_mame + pol_ata)

    def daj_glas(self):
        print(self.veselje * self.glas + '!')

    def razveseli(self):
        self.veselje += 1
    
    def __iter__(self):
        x = self.glas + '!'
        n = self.veselje
        return Ponavljalec(x, n)
