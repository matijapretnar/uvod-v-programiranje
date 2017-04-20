class Pes:

    def __init__(self, glas='hov', veselje=1):
        self.veselje = veselje
        self.glas = glas

    def __str__(self):
        if self.veselje > 10:
            return 'zelo vesel pes'
        elif self.veselje >= 1:
            return 'vesel pes'
        else:
            return 'depresiven pes'

    def __repr__(self):
        return "Pes(veselje={0}, glas={1!r})".format(self.veselje, self.glas)

    def daj_glas(self):
        print(self.veselje * self.glas + '!')

    def razveseli(self):
        self.veselje += 1

    
fido = Pes(veselje=10)
runo = Pes()
