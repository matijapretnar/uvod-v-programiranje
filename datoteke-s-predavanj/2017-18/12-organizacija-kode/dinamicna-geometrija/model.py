class Tocka:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        x, y = self.koordinate()
        return '{}(x={}, y={})'.format(self.__class__.__name__, x, y)

    def koordinate(self):
        return self.x, self.y

    def slika_na_platnu(self, platno):
        POLMER_TOCKE = 8
        x, y = self.koordinate()
        return platno.create_oval(
            x - POLMER_TOCKE,
            y - POLMER_TOCKE,
            x + POLMER_TOCKE,
            y + POLMER_TOCKE,
            activefill='blue',
            activeoutline='blue',
            fill='white',
        )


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

    def slika_na_platnu(self, platno):
        a, b, c = self.parametri()
        x1 = 0
        y1 = (c - a * x1) / b
        x2 = platno.winfo_width()
        y2 = (c - a * x2) / b
        return platno.create_line(
            x1,
            y1,
            x2,
            y2,
            activefill='blue',
        )


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
        c = a * x + b * y
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
        c = a * x + b * y
        return (a, b, c)


class Kroznica:
    def __init__(self, sredisce, polmer):
        self.sredisce = sredisce
        self.polmer = polmer

    def parametri(self):
        return self.sredisce, self.polmer

    def slika_na_platnu(self, platno):
        sredisce, polmer = self.parametri()
        x, y = sredisce.koordinate()
        return platno.create_oval(
            x - polmer,
            y - polmer,
            x + polmer,
            y + polmer,
            activeoutline='blue',
        )


class KroznicaSkoziTocki(Kroznica):
    def __init__(self, sredisce, obodna):
        self.sredisce = sredisce
        self.obodna = obodna

    def parametri(self):
        x1, y1 = self.sredisce.koordinate()
        x2, y2 = self.obodna.koordinate()
        r = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        return self.sredisce, r


class PreseciscePremiceInKroznice(Tocka):
    def __init__(self, premica, kroznica, je_prvo):
        self.premica = premica
        self.kroznica = kroznica
        self.je_prvo = je_prvo

    def koordinate(self):
        a x + b y = c
        (x - x0)^2 + (y - y0)^2 = r^2

        y = (c - a x) / b

        (x - x0)^2 + ((c - a x) / b - y0)^2 = r^2
        x^2 - 2 x0 x + x0^2 + (c / b - y0 - a / b x)^2 = r^2
        x^2 - 2 x0 x + x0^2 + (a^2 / b^2) x^2 + (c / b - y0)^2 - a / b x)^2 = r^2

        (x - x0)

        x1, y1 = self.sredisce.koordinate()
        x2, y2 = self.obodna.koordinate()
        r = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        return self.sredisce, r
