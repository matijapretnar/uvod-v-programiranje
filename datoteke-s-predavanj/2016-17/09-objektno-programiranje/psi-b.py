class Pes:
    def __init__(self, veselje=1, glas='hov'):
        self.veselje = veselje
        self.glas = glas
    def __repr__(self):
        return "Pes(veselje={0}, glas={1!r})".format(self.veselje, self.glas)
    def __str__(self):
        return "Pes z veseljem {0}, ki dela {1}".format(self.veselje, self.glas)
    def __lt__(self, other):
        return False
    def __destruct__(self):
        self.veselje = 0
        self.glas = None
    def daj_glas(self):
        print(self.veselje * self.glas + '!')
    def razveseli(self):
        self.veselje += 1
    def nauci_se_novega_glasu(self, nov_glas):
        self.glas = nov_glas

fido = Pes()
runo = Pes()