class Tocka:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def koordinate(self):
        return self.x, self.y

    def __str__(self):
        x, y = self.koordinate()
        return '({}, {})'.format(x, y)


class Premica:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        a, b, c = self.parametri()
        return '({} x + {} y + {} = 0)'.format(a, b, c)

    def parametri(self):
        return self.a, self.b, self.c


class PremicaSkoziTocki(Premica):
    def __init__(self, tocka1, tocka2):
        self.tocka1 = tocka1
        self.tocka2 = tocka2

    def parametri(self):
        x1, y1 = self.tocka1.koordinate()
        x2, y2 = self.tocka2.koordinate()
        if (x1, y1) != (x2, y2):
            a = y2 - y1
            b = x1 - x2
            c = - (a * x1 + b * y1)
            return a, b, c


class Presecisce(Tocka):
    def __init__(self, premica1, premica2):
        self.premica1 = premica1
        self.premica2 = premica2

    def koordinate(self):
        a1, b1, c1 = self.premica1.parametri()
        a2, b2, c2 = self.premica2.parametri()
        x = b1 * c2 - b2 * c1
        y = a2 * c1 - a1 * c2
        w = a1 * b2 - a2 * b1
        if w != 0:
            return x / w, y / w


tocka1 = Tocka(x=2, y=3)
tocka2 = Tocka(x=3, y=2)
tocka3 = Tocka(x=3, y=4)
tocka4 = Tocka(x=2, y=7)
p = PremicaSkoziTocki(tocka1, tocka2)
q = PremicaSkoziTocki(tocka3, tocka4)
x = Presecisce(p, q)
print(x)
