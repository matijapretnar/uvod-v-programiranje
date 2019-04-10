class ZbirkaVprasanj:
    def __init__(self, ime):
        self.ime = ime
        self.vprasanja = []

class Vprasanje:
    def __init__(self, besedilo, zbirka):
        self.besedilo = besedilo
        self.zbirka = zbirka
        self.odgovori = []
        self.zbirka.vprasanja.append(self)

class Odgovor:
    def __init__(self, besedilo, vprasanje):
        self.besedilo = besedilo
        self.vprasanje = vprasanje
        self.vprasanje.odgovori.append(self)

z = ZbirkaVprasanj(ime='UVP 2018/19')

v1 = Vprasanje(besedilo='Koliko je 1 + 1', zbirka=z)

o11 = Odgovor('1', vprasanje=v1)
o12 = Odgovor('2', vprasanje=v1)
o13 = Odgovor('1+1', vprasanje=v1)

v2 = Vprasanje(besedilo='Koliko je 2 + 2', zbirka=z)

o21 = Odgovor('1', vprasanje=v2),
o22 = Odgovor('2', vprasanje=v2),
o23 = Odgovor('4', vprasanje=v2),
o24 = Odgovor('2+2', vprasanje=v2),
