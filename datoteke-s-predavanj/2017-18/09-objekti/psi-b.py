class Pes:
    def __init__(self, glas='hov'):
        self.veselje = 1
        self.glas = glas

    def __repr__(self):
        return 'Pes(glas={0!r})'.format(
            self.glas
        )

    def __str__(self):
        return 'Pes, ki dela {0}.'.format(
            self.glas
        )

    def __add__(self, other):
        pol_mame = self.glas[:len(self.glas) // 2]
        pol_ata = other.glas[len(other.glas) // 2:]
        glas_novega_psa = pol_mame + pol_ata
        dete = Pes(glas=glas_novega_psa)
        dete.veselje = min(self.veselje, other.veselje)
        return dete

    def daj_glas(self):
        print(self.veselje * self.glas + '!')

    def razveseli(self):
        self.veselje += 1
