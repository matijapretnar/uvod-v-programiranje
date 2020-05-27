class NotranjiPes:
    def __init__(self, glas='hov'):
        self.jedilnik = []
        self.glas = glas

    def daj_glas(self):
        print(f'Pojedel sem: {", ".join(self.jedilnik)}')

    def pojej(self, hrana):
        self.jedilnik.append(hrana)


class ZunanjiPes:
    jedilnik = []

    def __init__(self, glas='hov'):
        self.glas = glas

    def daj_glas(self):
        print(f'Pojedel sem: {", ".join(self.jedilnik)}')

    def pojej(self, hrana):
        self.jedilnik.append(hrana)

fido1 = ZunanjiPes()
runo1 = ZunanjiPes()
fido2 = NotranjiPes()
runo2 = NotranjiPes()