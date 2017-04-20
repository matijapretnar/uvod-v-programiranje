class TekociRacun:
    def __init__(self, stevilka, stanje=0):
        self.stevilka = stevilka
        self.stanje = stanje
    def __repr__(self):
        return 'TekociRacun({0}, stanje={1})'.format(self.stevilka, self.stanje)
    def __str__(self):
        return 'račun št. {0} (stanje: {1} EUR)'.format(self.stevilka, self.stanje)
