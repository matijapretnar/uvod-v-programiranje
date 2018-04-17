class Pes:
    def __init__(self, glas='hov'):
        self.veselje = 1
        self.glas = glas

    def __repr__(self):
        return "Pes(glas={!r})".format(self.glas)

    def __str__(self):
        return 'Pes, ki dela {0}.'.format(
            self.glas
        )

    def daj_glas(self):
        print(self.veselje * self.glas + '!')

    def razveseli(self):
        self.veselje += 1
