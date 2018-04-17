POMEMBNE_OSEBE = ['Matija Pretnar']
OSNOVNI_LIMIT = 300
OSNOVNA_OBRESTNA_MERA = 0.0008


class Racun:
    def __init__(self, lastnik, stevilka):
        self.stanje = 0
        self.lastnik = lastnik
        self.stevilka = stevilka
        self.limit = OSNOVNI_LIMIT
        self.obrestna_mera = OSNOVNA_OBRESTNA_MERA

    def __str__(self):
        return '{}: {:.2f} EUR'.format(self.stevilka, self.stanje)

    def __repr__(self):
        return '<Racun: {}>'.format(str(self))

    def polozi(self, znesek):
        if znesek <= 0:
            raise ValueError('Znesek pologa mora biti pozitiven!')
        self.stanje += znesek

    def dvigni(self, znesek):
        if znesek > self.stanje + self.limit:
            raise ValueError('Znesek dviga presega stanje računa!')
        self.stanje -= znesek

    def spremeni_limit(self, limit):
        if self.lastnik not in POMEMBNE_OSEBE:
            raise ValueError('Lastnik ni dovolj pomemben, da bi mu spremenili limit!')
        self.limit = limit

    def obracunaj_obresti(self):
        if self.stanje > 0:
            self.stanje *= 1 + self.obrestna_mera
        else:
            self.stanje *= 1 + (10 * self.obrestna_mera)


tekoci = Racun('Matija Pretnar', 'SI56 1234 5678 9012 345')
tekoci.polozi(150)
tekoci.obracunaj_obresti()
tekoci.dvigni(150)
print(tekoci)
