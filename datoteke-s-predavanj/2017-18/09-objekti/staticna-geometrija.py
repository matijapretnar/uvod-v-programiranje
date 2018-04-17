class Tocka:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Tocka(x={}, y={})'.format(self.x, self.y)


class Premica:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __repr__(self):
        return 'Premica(a={}, b={}, c={})'.format(self.a, self.b, self.c)

    def pravokotnica(self, tocka):
        a = -self.b
        b = self.a
        c = -(a * tocka.x + b * tocka.y)
        return Premica(a, b, c)

    def presecisce(self, other):
        a1, b1, c1 = self.a, self.b, self.c
        a2, b2, c2 = other.a, other.b, other.c
        x = b1 * c2 - b2 * c1
        y = a2 * c1 - a1 * c2
        w = a1 * b2 - a2 * b1
        if w != 0:
            return Tocka(x / w, y / w)


t = Tocka(1, 1)
p = Premica(1, 0, 0)
q = p.pravokotnica(t)
u = p.presecisce(q)
