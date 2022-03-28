class SprehajalecPoRazponu:
    def __init__(self, m, n):
        self.kje_sem = m
        self.kje_bom_koncal = n
    
    def __next__(self):
        if self.kje_sem < self.kje_bom_koncal:
            self.kje_sem += 1
            return self.kje_sem - 1
        else:
            raise StopIteration

class SprehajalecPoNizu:
    def __init__(self, niz):
        self.kje_sem = 0
        self.kje_bom_koncal = len(niz)
        self.niz = niz
    
    def __next__(self):
        if self.kje_sem < self.kje_bom_koncal:
            self.kje_sem += 1
            return self.niz[self.kje_sem - 1]
        else:
            raise StopIteration
    
    def __iter__(self):
        return self

class Razpon:
    def __init__(self, od, do):
        self.od = od
        self.do = do

    def __iter__(self):
        sprehajalec = SprehajalecPoRazponu(self.od, self.do)
        return sprehajalec


def fibonacci(m):
    a, b = 0, 1
    while a <= m:
        yield a
        a, b = b, a + b
