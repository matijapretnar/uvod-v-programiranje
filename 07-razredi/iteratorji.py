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

class Razpon:
    def __init__(self, od, do):
        self.od = od
        self.do = do
        x = 10

    def __iter__(self):
        sprehajalec = SprehajalecPoRazponu(self.od, self.do)
        return sprehajalec
