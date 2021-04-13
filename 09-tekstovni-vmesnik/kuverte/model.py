class Model:
    def __init__(self):
        self.kuverte = []
        self.racuni = []
    
    def dodaj_kuverto(self, kuverta):
        self.kuverte.append(kuverta)

    def dodaj_racun(self, racun):
        self.racuni.append(racun)


class Kuverta:
    def __init__(self, ime):
        self.ime = ime
        self.transakcije = []

    def stanje(self):
        return sum(transakcija.znesek for transakcija in self.transakcije)
    
    def dodaj_transakcijo(self, transakcija):
        self.transakcije.append(transakcija)

class Racun:
    def __init__(self, ime):
        self.ime = ime
        self.transakcije = []

    def stanje(self):
        return sum(transakcija.znesek for transakcija in self.transakcije)
    
    def dodaj_transakcijo(self, transakcija):
        self.transakcije.append(transakcija)

class Transakcija:
    def __init__(self, znesek, opis, datum):
        self.znesek = znesek
        self.opis = opis
        self.datum = datum
