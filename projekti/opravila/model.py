import json


class Stanje:
    def __init__(self, kategorije):
        self.kategorije = kategorije

    def dodaj_kategorijo(self, kategorija):
        self.kategorije.append(kategorija)

    def v_slovar(self):
        return {
            "kategorije": [kategorija.v_slovar() for kategorija in self.kategorije],
        }

    @staticmethod
    def iz_slovarja(slovar):
        stanje = Stanje(
            [
                Kategorija.iz_slovarja(sl_kategorije)
                for sl_kategorije in slovar["kategorije"]
            ]
        )
        return stanje

    def shrani_v_datoteko(self, ime_datoteke):
        with open(ime_datoteke, "w") as dat:
            slovar = self.v_slovar()
            json.dump(slovar, dat, indent=4, ensure_ascii=False)

    @staticmethod
    def preberi_iz_datoteke(ime_datoteke):
        with open(ime_datoteke) as dat:
            slovar = json.load(dat)
            return Stanje.iz_slovarja(slovar)


class Kategorija:
    def __init__(self, ime, opravila):
        self.ime = ime
        self.opravila = opravila

    def stevilo_neopravljenih(self):
        neopravljena = 0
        for opravilo in self.opravila:
            if not opravilo.opravljeno:
                neopravljena += 1
        return neopravljena

    def dodaj_opravilo(self, opravilo):
        self.opravila.append(opravilo)

    def v_slovar(self):
        return {
            "ime": self.ime,
            "opravila": [opravilo.v_slovar() for opravilo in self.opravila],
        }

    @staticmethod
    def iz_slovarja(slovar):
        return Kategorija(
            slovar["ime"],
            [Opravilo.iz_slovarja(sl_opravila) for sl_opravila in slovar["opravila"]],
        )


class Opravilo:
    def __init__(self, opis, opravljeno=False):
        self.opis = opis
        self.opravljeno = opravljeno

    def opravi(self):
        self.opravljeno = True

    def v_slovar(self):
        return {
            "opis": self.opis,
            "opravljeno": self.opravljeno,
        }

    @staticmethod
    def iz_slovarja(slovar):
        return Opravilo(
            slovar["opis"],
            slovar["opravljeno"],
        )
