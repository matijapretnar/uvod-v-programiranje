from datetime import date
import json


class Model:
    def __init__(self):
        self.spiski = []
        self.aktualni_spisek = None

    def dodaj_spisek(self, spisek):
        self.spiski.append(spisek)
        if not self.aktualni_spisek:
            self.aktualni_spisek = spisek

    def pobrisi_spisek(self, spisek):
        self.spiski.remove(spisek)

    def zamenjaj_spisek(self, spisek):
        self.aktualni_spisek = spisek

    def dodaj_opravilo(self, opravilo):
        self.aktualni_spisek.dodaj_opravilo(opravilo)

    def pobrisi_opravilo(self, opravilo):
        self.aktualni_spisek.pobrisi_opravilo(opravilo)

    def stevilo_zamujenih(self):
        return sum([spisek.stevilo_zamujenih() for spisek in self.spiski])

    def v_slovar(self):
        return {
            "spiski": [spisek.v_slovar() for spisek in self.spiski],
            "aktualni_spisek": self.spiski.index(self.aktualni_spisek)
            if self.aktualni_spisek
            else None,
        }

    @staticmethod
    def iz_slovarja(slovar):
        model = Model()
        model.spiski = [Spisek.iz_slovarja(sl_spiska) for sl_spiska in slovar["spiski"]]
        if slovar["aktualni_spisek"] is not None:
            model.aktualni_spisek = model.spiski[slovar["aktualni_spisek"]]
        return model

    def shrani_v_datoteko(self, ime_datoteke):
        with open(ime_datoteke, "w") as dat:
            slovar = self.v_slovar()
            json.dump(slovar, dat)

    @staticmethod
    def preberi_iz_datoteke(ime_datoteke):
        with open(ime_datoteke) as dat:
            slovar = json.load(dat)
            return Model.iz_slovarja(slovar)


class Spisek:
    def __init__(self, ime):
        self.ime = ime
        self.opravila = []

    def dodaj_opravilo(self, opravilo):
        self.opravila.append(opravilo)

    def stevilo_zamujenih(self):
        stevilo = 0
        for opravilo in self.opravila:
            if opravilo.zamuja():
                stevilo += 1
        return stevilo

    def stevilo_vseh(self):
        return len(self.opravila)

    def v_slovar(self):
        return {
            "ime": self.ime,
            "opravila": [opravilo.v_slovar() for opravilo in self.opravila],
        }

    @staticmethod
    def iz_slovarja(slovar):
        spisek = Spisek(slovar["ime"])
        spisek.opravila = [
            Opravilo.iz_slovarja(sl_opravila) for sl_opravila in slovar["opravila"]
        ]
        return spisek


class Opravilo:
    def __init__(self, ime, opis, rok, opravljeno=False):
        self.ime = ime
        self.opis = opis
        self.rok = rok
        self.opravljeno = opravljeno

    def opravi(self):
        self.opravljeno = True

    def zamuja(self):
        rok_pretekel = self.rok and self.rok < date.today()
        return not self.opravljeno and rok_pretekel

    def v_slovar(self):
        return {
            "ime": self.ime,
            "opis": self.opis,
            "rok": date.isoformat(self.rok) if self.rok else None,
            "opravljeno": self.opravljeno,
        }

    @staticmethod
    def iz_slovarja(slovar):
        return Opravilo(
            slovar["ime"],
            slovar["opis"],
            date.fromisoformat(slovar["rok"]) if slovar["rok"] else None,
            slovar["opravljeno"],
        )
