import datetime

class ZbirkaVprasanj:
    def __init__(self, ime, vprasanja):
        self.ime = ime
        self.vprasanja = vprasanja
        self.trenutno_vprasanje = None
    
    def odpri_vprasanje(self, indeks_vprasanja):
        self.trenutno_vprasanje = self.vprasanja[indeks_vprasanja]
    
    def zapri_trenutno_vprasanje(self):
        self.trenutno_vprasanje = None


class Vprasanje:
    def __init__(self, besedilo, odgovori):
        self.besedilo = besedilo
        self.odgovori = odgovori
    
    def glasuj_za_odgovor(self, indeks_odgovora):
        self.odgovori[indeks_odgovora].glasuj()

class Odgovor:
    def __init__(self, besedilo):
        self.besedilo = besedilo
        self.glasovi = []
    
    def glasuj(self):
        self.glasovi.append(Glas())

class Glas:
    def __init__(self):
        self.cas = datetime.datetime.now()

o = Odgovor(besedilo='42')
o.glasuj()
o.glasuj()
o.glasuj()
o.glasuj()




# ZbirkaVprasanj(
#     ime='UVP 2018/19',
#     vprasanja=[
#         Vprasanje(
#             besedilo='Koliko je 1 + 1',
#             odgovori=[
#                 Odgovor('1'),
#                 Odgovor('2'),
#                 Odgovor('1+1'),
#             ]
#         ),
#         Vprasanje(
#             besedilo='Koliko je 2 + 2',
#             odgovori=[
#                 Odgovor('1'),
#                 Odgovor('2'),
#                 Odgovor('4'),
#                 Odgovor('2+2'),
#             ]
#         )
#     ]
# )

# o11 = Odgovor('1')
# o12 = Odgovor('2')
# o13 = Odgovor('1+1')

# v1 = Vprasanje(
#     besedilo='Koliko je 1 + 1',
#     odgovori=[o11, o12, o13]
# )

# o21 = Odgovor('1')
# o22 = Odgovor('2')
# o23 = Odgovor('4')
# o24 = Odgovor('2+2')

# v2 = Vprasanje(
#     besedilo='Koliko je 2 + 2',
#     odgovori=[o21, o22, o23, o24]
# )

# z = ZbirkaVprasanj(
#     ime='UVP 2018/19',
#     vprasanja=[v1, v2]
# )
