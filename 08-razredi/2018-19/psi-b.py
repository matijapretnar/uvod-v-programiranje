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
            

class Ponavljalec2:
    def __init__(self, x, y, n):
        self.x = x
        self.y = y
        self.n = n

    def __next__(self):
        if self.n > 0:
            self.n -= 1
            self.y, self.x = self.x, self.y
            return self.y
        else:
            raise StopIteration
    
    #             |
    #             V
    # 1 2 3 4 5 6 7 8 9

    def __iter__(self):
        return self
            

class Pes:
    def __init__(self, glas='hov'):
        self.veselje = 1
        self.glas = glas
    
    def __lt__(self, other):
        return self.veselje < other.veselje
    
    def __contains__(self, x):
        return x == 'klobasa'
    
    def __repr__(self):
        return "Pes(glas={})".format(repr(self.glas))
    
    def __iter__(self):
        for i in range(self.veselje):
            if i % 2 == 0:
                yield self.glas + '!'
            else:
                yield 'ham ham'
    
    def __str__(self):
        return 'En pes'

    def daj_glas(self):
        print(self.veselje * self.glas + '!')

    def razveseli(self):
        self.veselje += 1

runo = Pes(glas='vuf')
runo.razveseli()
runo.razveseli()
runo.daj_glas()
