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

    def nova_kuverta(self, ime):
        for kuverta in self.kuverte:
            if kuverta.ime == ime:
                raise ValueError('Račun s tem imenom že obstaja!')
        nova = Kuverta(ime, 0, self)
        self.kuverte.append(nova)
        return nova
    
    def nov_preliv(self, znesek, datum, opis, racun, kuverta):
        if racun.proracun != self:
            raise ValueError(f'Račun {racun} ne spada v ta proračun!')
        elif kuverta is not None and kuverta.proracun != self:
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
    
    def nerazporejena_sredstva(self):
        vrednost_nerazporejenih_prelivov = sum(preliv.znesek for preliv in self.prelivi if preliv.kuverta is None)
        razporeditev_v_kuverte = sum(kuverta.dodeljeno_stanje for kuverta in self.kuverte)
        return vrednost_nerazporejenih_prelivov - razporeditev_v_kuverte

class Racun:
    def __init__(self, ime, proracun):
        self.ime = ime
        self.proracun = proracun
    
    def __repr__(self):
        return f'<Racun: {self}>'

    def __str__(self):
        return f'{self.ime}: {self.stanje()}€'

    def stanje(self):
        return sum([preliv.znesek for preliv in self.prelivi()])

    def v_slovar(self):
        return {
            'ime': self.ime,
        }
    
    def prelivi(self):
        for preliv in self.proracun.prelivi:
            if preliv.racun == self:
                yield preliv


class Kuverta:
    def __init__(self, ime, dodeljeno_stanje, proracun):
        self.ime = ime
        self.proracun = proracun
        self.dodeljeno_stanje = dodeljeno_stanje
    
    def __str__(self):
        return f'{self.ime}: {self.stanje()}€'

    def stanje(self):
        return self.dodeljeno_stanje + sum([preliv.znesek for preliv in self.prelivi()])

    def v_slovar(self):
        return {
            'ime': self.ime,
        }

    def prelivi(self):
        for preliv in self.proracun.prelivi:
            if preliv.kuverta == self:
                yield preliv

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
            'kuverta': None if self.kuverta is None else self.kuverta.ime,
        }