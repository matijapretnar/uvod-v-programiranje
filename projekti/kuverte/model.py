class Proracun:
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
        self.prelivi = []

    def stanje(self):
        return sum(preliv.znesek for preliv in self.prelivi)
    
    def dodaj_preliv(self, preliv):
        self.prelivi.append(preliv)

class Racun:
    def __init__(self, ime):
        self.ime = ime
        self.prelivi = []

    def stanje(self):
        return sum(preliv.znesek for preliv in self.prelivi)
    
    def dodaj_preliv(self, preliv):
        self.prelivi.append(preliv)

class Preliv:
    def __init__(self, znesek, datum, opis, racun, kuverta):
        self.znesek = znesek
        self.datum = datum
        self.opis = opis
        self.racun = racun
        self.kuverta = kuverta
