class Proracun:
    def __init__(self):
        self.racuni = []
        self.kuverte = []
        self.prelivi = []

    def nov_racun(self, ime):
        for racun in self.racuni:
            if racun.ime == ime:
                raise ValueError('Račun s tem imenom že obstaja!')
        nov = Racun(ime, self)
        self.racuni.append(nov)
        return nov

    def nov_kuverto(self, ime):
        for kuverta in self.kuverte:
            if kuverta.ime == ime:
                raise ValueError('Račun s tem imenom že obstaja!')
        nova = Kuverta(ime, self)
        self.kuverte.append(nova)
        return nova
    
    def nov_preliv(self, znesek, datum, opis, racun, kuverta):
        if racun.proracun != self:
            raise ValueError(f'Račun {racun} ne spada v ta proračun!')
        elif kuverta.proracun != self:
            raise ValueError(f'Kuverta {kuverta} ne spada v ta proračun!')
        else:
            nov = Preliv(znesek, datum, opis, racun, kuverta)
            self.prelivi.append(nov)
            return nov


    def __str__(self):
        return f'Računi: {self.racuni}'

    def v_slovar(self):
        return {
            'racuni': [racun.v_slovar() for racun in self.racuni],
            'kuverte': [kuverta.v_slovar() for kuverta in self.kuverte],
            'prelivi': [preliv.v_slovar() for preliv in self.prelivi],
        }

class Racun:
    def __init__(self, ime, proracun):
        self.ime = ime
        self.proracun = proracun
    
    def __repr__(self):
        return f'<Racun: {self}>'

    def __str__(self):
        return f'{self.ime}: {self.stanje()}€'

    def stanje(self):
        return sum([preliv.znesek for preliv in self.prelivi])

    def v_slovar(self):
        return {
            'ime': self.ime,
        }


class Kuverta:
    def __init__(self, ime, proracun):
        self.ime = ime
        self.proracun = proracun
    
    def __str__(self):
        return f'{self.ime}: {self.stanje()}€'

    def stanje(self):
        return sum([preliv.znesek for preliv in self.prelivi])

    def v_slovar(self):
        return {
            'ime': self.ime,
        }

class Preliv:
    def __init__(self, znesek, datum, opis, racun, kuverta):
        self.znesek = znesek
        self.datum = datum
        self.opis = opis
        self.racun = racun
        self.kuverta = kuverta

    def v_slovar(self):
        return {
            'znesek': self.znesek,
            'datum': str(self.datum),
            'opis': self.opis,
            'racun': self.racun.ime,
            'kuverta': self.kuverta.ime,
        }