import datetime


class ZbirkaVprasanj:
    def __init__(self, ime, vprasanja):
        self.ime = ime
        self.vprasanja = vprasanja
        self.trenutno_vprasanje = None

    def besedilo_trenutnega_vprasanja(self):
        if self.trenutno_vprasanje == None:
            return None
        else:
            return self.trenutno_vprasanje.besedilo

    def odpri_vprasanje(self, indeks_vprasanja):
        self.trenutno_vprasanje = self.vprasanja[indeks_vprasanja]

    def zapri_trenutno_vprasanje(self):
        self.trenutno_vprasanje = None

    def glasuj(self, indeks_odgovora):
        self.trenutno_vprasanje.glasuj_za_odgovor(indeks_odgovora)

    def dodaj_vprasanje(self, besedilo_vprasanja, besedila_odgovorov):
        self.vprasanja.append(Vprasanje(besedilo_vprasanja, [Odgovor(odgovor) for odgovor in besedila_odgovorov]))

    def podvoji_vprasanje(self, indeks_vprasanja):
        self.vprasanja.append(self.vprasanja[indeks_vprasanja].podvoji())


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
