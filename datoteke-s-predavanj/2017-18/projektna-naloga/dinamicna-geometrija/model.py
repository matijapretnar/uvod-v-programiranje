class Tocka:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        x, y = self.koordinate()
        return '{}(x={}, y={})'.format(self.__class__.__name__, x, y)

    def koordinate(self):
        return self.x, self.y


class Premica:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __repr__(self):
        a, b, c = self.parametri()
        return '{}(a={}, b={}, c={})'.format(self.__class__.__name__, a, b, c)

    def parametri(self):
        return self.a, self.b, self.c


class PremicaSkoziTocki(Premica):
    def __init__(self, tocka1, tocka2):
        self.tocka1 = tocka1
        self.tocka2 = tocka2

    def parametri(self):
        x1, y1 = self.tocka1.koordinate()
        x2, y2 = self.tocka2.koordinate()
        a = y1 - y2
        b = x2 - x1
        c = a * x1 + b * y1
        return a, b, c


class PreseciscePremic(Tocka):
    def __init__(self, premica1, premica2):
        self.premica1 = premica1
        self.premica2 = premica2

    def koordinate(self):
        a1, b1, c1 = self.premica1.parametri()
        a2, b2, c2 = self.premica2.parametri()
        x = b1 * c2 - b2 * c1
        y = a2 * c1 - a1 * c2
        w = a2 * b1 - a1 * b2
        if w != 0:
            return (x / w, y / w)


class Pravokotnica(Premica):
    def __init__(self, premica, tocka):
        self.premica = premica
        self.tocka = tocka

    def parametri(self):
        a0, b0, _ = self.premica.parametri()
        a = -b0
        b = a0
        x, y = self.tocka.koordinate()
        c = -(a * x + b * y)
        return (a, b, c)


class Vzporednica(Premica):
    def __init__(self, premica, tocka):
        self.premica = premica
        self.tocka = tocka

    def parametri(self):
        a0, b0, _ = self.premica.parametri()
        a = a0
        b = b0
        x, y = self.tocka.koordinate()
        c = -(a * x + b * y)
        return (a, b, c)


class Konstrukcija:
    def __init__(self):
        self.tocke = []
        self.premice = []

    def dodaj_tocko(self, tocka):
        self.tocke.append(tocka)

    def dodaj_premico(self, premica):
        self.premice.append(premica)
