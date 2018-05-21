import random
DESNO, GOR, DOL, LEVO = 'desno', 'gor', 'dol', 'levo'

class Kaca:
    def __init__(self, tocke, smer=DESNO):
        self.tocke = tocke
        self.smer = smer

    def __repr__(self):
        if self.smer == DESNO:
            opis_smeri = 'DESNO'
        elif self.smer == GOR:
            opis_smeri = 'GOR'
        elif self.smer == DOL:
            opis_smeri = 'DOL'
        elif self.smer == LEVO:
            opis_smeri = 'LEVO'
        return 'Kaca({}, smer={})'.format(self.tocke, opis_smeri)

    def nova_glava(self):
        glava_x, glava_y = self.tocke[0]
        if self.smer == DESNO:
            glava_x += 1
        elif self.smer == GOR:
            glava_y -= 1
        elif self.smer == DOL:
            glava_y += 1
        elif self.smer == LEVO:
            glava_x -= 1
        return glava_x, glava_y

    def premakni(self):
        del self.tocke[-1]
        self.tocke.insert(0, self.nova_glava())

    def zrasti(self):
        self.tocke.insert(0, self.nova_glava())

    def zamenjaj_smer(self, nova_smer):
        if {nova_smer, self.smer} not in [{GOR, DOL}, {LEVO, DESNO}]:
            self.smer = nova_smer


class Igra:
    def __init__(self, sirina, visina):
        self.sirina = sirina
        self.visina = visina

        # vodoravno kačo dolžine 3 nastavimo na naključno mesto na plošči
        x, y = random.randrange(self.sirina - 2), random.randrange(self.visina)
        self.kaca = Kaca([(x + 2, y), (x + 1, y), (x, y)])

        self.postavi_jabolko()


    def __str__(self):
        polja = []
        for _ in range(self.visina):
            polja.append(self.sirina * [' '])
        if self.je_kaca_v_redu():
            for i, (x, y) in enumerate(self.kaca.tocke):
                polja[y][x] = str(i % 10)
        x_jabolko, y_jabolko = self.jabolko
        polja[y_jabolko][x_jabolko] = '@'
        rob = '+{}+'.format(self.sirina * '-')
        izpis = ''
        for vrstica in polja:
            izpis += '|{}|\n'.format(''.join(vrstica))
        return '{}\n{}{}'.format(rob, izpis, rob)

    def postavi_jabolko(self):
        # poiščemo mesto za jabolko, ki ne leži na kači
        while True:
            self.jabolko = random.randrange(self.sirina), random.randrange(self.visina)
            if self.jabolko not in self.kaca.tocke:
                break


    def je_kaca_v_redu(self):
        for x, y in self.kaca.tocke:
            # preverimo, ali je celotna kača na plošči
            if not (0 <= x < self.sirina and 0 <= y < self.visina):
                return False

        # preverimo, da kača ne seka same sebe, torej ima vse točke različne
        return len(self.kaca.tocke) == len(set(self.kaca.tocke))

    def kaca_je_pojedla_jabolko(self):
        return self.kaca.tocke[0] == self.jabolko

    def naredi_korak(self):
        if self.kaca_je_pojedla_jabolko():
            self.kaca.zrasti()
            self.postavi_jabolko()
        else:
            self.kaca.premakni()

    def tezavnost(self):
        '''Vrne število korakov, ki jih v sekundi naredi kača.'''
        return len(self.kaca.tocke)

igra = Igra(10, 10)