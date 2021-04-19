from datetime import date

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

class Opravilo:
    def __init__(self, ime, opis, rok):
        self.ime = ime
        self.opis = opis
        self.rok = rok
        self.opravljeno = False

    def opravi(self):
        self.opravljeno = True
    
    def zamuja(self):
        rok_pretekel = self.rok and self.rok < date.today()
        return not self.opravljeno and rok_pretekel
