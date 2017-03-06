class Vektor:
    '''
    Razred Vektor predstavlja vektorje v tri-razsežnem prostoru.

    Razred podpira cel kup operacij nad vektorji.
    '''

    def __init__(self, x, y, z):
        self.komponente = (x, y, z)

    def __repr__(self):
        x, y, z = self.komponente
        return 'Vektor({}, {}, {})'.format(x, y, z)

    def __add__(self, other):
        x1, y1, z1 = self.komponente
        x2, y2, z2 = other.komponente
        return Vektor(x1 + x2, y1 + y2, z1 + z2)

    def __sub__(self, other):
        x1, y1, z1 = self.komponente
        x2, y2, z2 = other.komponente
        return Vektor(x1 - x2, y1 - y2, z1 - z2)

    def __mul__(self, other):
        if isinstance(other, Vektor):
            x1, y1, z1 = self.komponente
            x2, y2, z2 = other.komponente
            return Vektor(x1 * y1 - z2 * x1, 5, 10)
        else:
            x, y, z = self.komponente
            return Vektor(x * other, y * other, z * other)

    def skalarni_produkt(self, other):
        '''Vrne skalarni produkt danih vektorjev.'''
        x1, y1, z1 = self.komponente
        x2, y2, z2 = other.komponente
        return x1 * x2 + y1 * y2 + z1 * z2
