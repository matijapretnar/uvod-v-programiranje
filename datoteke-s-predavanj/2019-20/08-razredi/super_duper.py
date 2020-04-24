class A:
    def metoda(self):
        print('A')


class B(A):
    def metoda(self):
        print('B')


class C(B):
    def metoda(self):
        print('C')
    
    def super_metoda(self):
        # vsi štirje klici pokličejo metodo iz razreda B
        super().metoda()
        super(C, self).metoda()
        super(type(c), self).metoda()
        super(type(c).mro()[0], self).metoda()

    def super_duper_metoda(self):
        # oba klica pokličeta metodo iz razreda A
        super(B, self).metoda()
        super(type(c).mro()[1], self).metoda()
