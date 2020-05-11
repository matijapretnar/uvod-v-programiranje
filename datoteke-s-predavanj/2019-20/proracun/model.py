class Proracun:
    def __init__(self):
        self.racuni = []
        self.kuverte = []

    def dodaj_racun(self, ime):
        return Racun(ime, self)

    def dodaj_kuverto(self, ime):
        return Kuverta(ime, self)
    
    def dodaj_preliv(self, znesek, datum, opis, racun, kuverta):
        if racun.proracun != self:
            print('Tole pa ni dobro!')
        elif kuverta.proracun != self:
            print('Tole pa ni dobro!')
        else:
            return Preliv(znesek, datum, opis, racun, kuverta)

    def __str__(self):
        return f'Računi: {self.racuni}'


class Racun:
    def __init__(self, ime, proracun):
        self.ime = ime
        self.proracun = proracun
        self.proracun.racuni.append(self)
        self.prelivi = []
    
    def __repr__(self):
        return f'<Racun: {self}>'

    def __str__(self):
        return f'{self.ime}: {self.stanje()}€'

    def stanje(self):
        return sum([preliv.znesek for preliv in self.prelivi])


class Kuverta:
    def __init__(self, ime, proracun):
        self.ime = ime
        self.proracun = proracun
        self.proracun.kuverte.append(self)
        self.prelivi = []
    
    def __str__(self):
        return f'{self.ime}: {self.stanje()}€'

    def stanje(self):
        return sum([preliv.znesek for preliv in self.prelivi])


class Preliv:
    def __init__(self, znesek, datum, opis, racun, kuverta):
        self.znesek = znesek
        self.datum = datum
        self.opis = opis
        self.racun = racun
        self.racun.prelivi.append(self)
        self.kuverta = kuverta
        self.kuverta.prelivi.append(self)
