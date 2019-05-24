import datetime
import json


class ZbirkaVprasanj:
    def __init__(self, ime, datoteka):
        self.ime = ime
        self.datoteka = datoteka
        self.vprasanja = [
            Vprasanje('Kakšno je danes vreme?', [
                Odgovor('sončno'),
                Odgovor('oblačno'),
                Odgovor('deževno'),
            ]),
            Vprasanje('Kakšno je bilo včeraj vreme?', [
                Odgovor('ne vem, sem bil ves dan na faksu'),
                Odgovor('mi je vseeno, sem matematik'),
            ]),
        ]            
        self.trenutno_vprasanje = self.vprasanja[0]
        self.nalozi()
    
    def v_slovar(self):
        return {
            'vprasanja': [vprasanje.v_slovar() for vprasanje in self.vprasanja]
        }
    
    def iz_slovarja(self, slovar):
        pass

    def shrani(self):
        with open(self.datoteka, 'w', encoding='utf-8') as datoteka:
            json.dump(self.v_slovar(), datoteka)
    
    def nalozi(self):
        pass
        # with open(self.datoteka, encoding='utf-8') as datoteka:
        #     self.iz_slovarja(json.load(datoteka))

    def odpri_vprasanje(self, indeks_vprasanja):
        self.trenutno_vprasanje = self.vprasanja[indeks_vprasanja]
        self.shrani()

    def zapri_trenutno_vprasanje(self):
        self.trenutno_vprasanje = None
        self.shrani()

    def glasuj(self, indeks_odgovora):
        self.trenutno_vprasanje.glasuj_za_odgovor(indeks_odgovora)
        self.shrani()

    def dodaj_vprasanje(self, besedilo_vprasanja, besedila_odgovorov):
        self.vprasanja.append(Vprasanje(besedilo_vprasanja, [Odgovor(odgovor) for odgovor in besedila_odgovorov]))
        self.shrani()

    def podvoji_vprasanje(self, indeks_vprasanja):
        self.vprasanja.append(self.vprasanja[indeks_vprasanja].podvoji())
        self.shrani()


class Vprasanje:
    def __init__(self, besedilo, odgovori):
        self.besedilo = besedilo
        self.odgovori = odgovori

    def glasuj_za_odgovor(self, indeks_odgovora):
        self.odgovori[indeks_odgovora].glasuj()

    def stevilo_glasov(self):
        stevilo = 0
        for odgovor in self.odgovori:
            stevilo += odgovor.stevilo_glasov()
        return stevilo

    def podvoji(self):
        return Vprasanje(self.besedilo, [odgovor.podvoji() for odgovor in self.odgovori])
    
    def v_slovar(self):
        return {
            'besedilo': self.besedilo,
            'odgovori': ['bla bla bla']
        }


class Odgovor:
    def __init__(self, besedilo):
        self.besedilo = besedilo
        self.glasovi = []

    def glasuj(self):
        self.glasovi.append(Glas())

    def stevilo_glasov(self):
        return len(self.glasovi)

    def podvoji(self):
        return Odgovor(self.besedilo)


class Glas:
    def __init__(self):
        self.cas = datetime.datetime.now()
