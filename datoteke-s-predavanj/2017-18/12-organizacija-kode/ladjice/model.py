import random

NAVPICNO = 'N'
VODORAVNO = 'V'

NEVELJAVNA_POTEZA = '?'
ZGRESENA = 'O'
ZADETA = 'X'
KONEC_IGRE = 'K'

class Plosca:
    def __init__(self, visina=20, sirina=20, dolzine_ladjic=[2, 2, 3, 4, 5]):
        self.visina = visina
        self.sirina = sirina
        self.ladjice = []
        for dolzina in dolzine_ladjic:
            self.nakljucno_polozi_ladjico(dolzina)
        self.izstrelki = set()
        self.poteze = 0

    def __repr__(self):
        return 'Plosca(visina={}, sirina={}, ladjice={})'.format(
            self.visina, self.sirina, self.ladjice
        )

    def __str__(self):
        polja = []
        for _ in range(self.visina):
            polja.append(self.sirina * [' '])

        for vrstica, stolpec in self.izstrelki:
            polja[vrstica][stolpec] = 'o'

        for n, ladjica in enumerate(self.ladjice):
            for vrstica, stolpec in ladjica.zasedena_polja():
                if (vrstica, stolpec) in self.izstrelki:
                    polja[vrstica][stolpec] = 'x'
                else:
                    polja[vrstica][stolpec] = str(n)

        niz = ''
        rob = '+' + self.sirina * '-' + '+\n'
        for vrstica in polja:
            niz += '|' + ''.join(vrstica) + '|\n'
        return rob + niz + rob

    def polozi_ladjico(self, ladjica):
        '''Ladjico z dano smerjo in poljem položi na ploščo.

        Če so vsa polja prosta, ladjico položi in vrne True,
        sicer ladjice ne položi in vrne False.
        '''
        if ladjica.zasedena_polja() & self.zasedena_polja():
            return False
        else:
            self.ladjice.append(ladjica)
            return True

    def nakljucno_polozi_ladjico(self, dolzina):
        ladjica_je_polozena = False
        while not ladjica_je_polozena:
            smer = random.choice([NAVPICNO, VODORAVNO])
            if smer == NAVPICNO:
                vrstica = random.randrange(self.visina - dolzina + 1)
                stolpec = random.randrange(self.sirina)
            elif smer == VODORAVNO:
                vrstica = random.randrange(self.visina)
                stolpec = random.randrange(self.sirina - dolzina + 1)
            ladjica = Ladjica((vrstica, stolpec), dolzina, smer)
            ladjica_je_polozena = self.polozi_ladjico(ladjica)

    def zasedena_polja(self):
        '''Vrne množico koordinat vseh polj, na katerih so ladjice.'''
        zasedena = set()
        for ladjica in self.ladjice:
            zasedena.update(ladjica.zasedena_polja())
        return zasedena

    def izstreli_izstrelek(self, vrstica, stolpec):
        '''Na koordinati (vrstica, stolpec) izstreli izstrelek.

        Vrne:
        - ZADETA, če je izstrelek zadel ladjo,
        - ZGRESENA, če je izstrelek zgrešil ladjo,
        - NEVELJAVNA_POTEZA, če poteza ni bila veljavna.
        V zadnjem primeru plošče ne spremeni.
        '''
        if 0 <= vrstica < self.visina and 0 <= stolpec < self.sirina and (vrstica, stolpec) not in self.izstrelki:
            self.poteze += 1
            self.izstrelki.add((vrstica, stolpec))
            for ladjica in self.ladjice:
                if (vrstica, stolpec) in ladjica.zasedena_polja():
                    if self.konec_igre():
                        return KONEC_IGRE
                    else:
                        return ZADETA
            return ZGRESENA
        else:
            return NEVELJAVNA_POTEZA

    def konec_igre(self):
        for ladjica in self.ladjice:
            for polje in ladjica.zasedena_polja():
                if polje not in self.izstrelki:
                    return False
        return True
        


class Ladjica:
    def __init__(self, polje, dolzina, smer):
        self.polje = polje
        self.dolzina = dolzina
        self.smer = smer

    def __repr__(self):
        return 'Ladjica({0}, {1}, {2})'.format(
            self.polje,
            self.dolzina,
            self.smer
        )

    def zasedena_polja(self):
        '''Vrne množico vseh polj, ki jih zaseda ladjica.'''
        zasedena = set()
        vrstica, stolpec = self.polje
        for i in range(self.dolzina):
            if self.smer == NAVPICNO:
                zasedena.add((vrstica + i, stolpec))
            elif self.smer == VODORAVNO:
                zasedena.add((vrstica, stolpec + i))
        return zasedena


plosca = Plosca(visina=10)
plosca.polozi_ladjico(Ladjica((2, 3), 10, VODORAVNO))
plosca.polozi_ladjico(Ladjica((5, 2), 2, NAVPICNO))
plosca.polozi_ladjico(Ladjica((1, 3), 4, VODORAVNO))
