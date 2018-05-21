RDECA, ZELENA, RUMENA = 'rdeca', 'zelena', 'rumena'

class SemaforModel:
    def __init__(self):
        self.barva = RDECA

    def daj_na_zeleno(self):
        self.barva = ZELENA

    def daj_na_rumeno(self):
        self.barva = RUMENA

    def daj_na_rdeco(self):
        self.barva = RDECA
