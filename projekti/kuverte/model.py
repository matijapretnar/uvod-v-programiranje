from dataclasses import dataclass
from datetime import date
from typing import List

@dataclass
class Transakcija:
    opis: str
    znesek: float
    datum: date

@dataclass
class ZbirkaTransakcij:
    ime: str
    transakcije: List[Transakcija]

    def __str__(self):
        return f"{self.ime}: {self.stanje()} €"

    def stanje(self):
        return sum(transakcija.znesek for transakcija in self.transakcije)

    def dodaj_transakcijo(self, transakcija):
        self.transakcije.append(transakcija)

class Kuverta(ZbirkaTransakcij):
    pass

class Racun(ZbirkaTransakcij):
    pass

@dataclass
class Stanje:
    kuverte: List[Kuverta]
    racuni: List[Racun]

od_babice = Transakcija("babica za desetko pri UVP", 100, date(2022, 4, 26))
iz_neba = Transakcija("priletelo iz neba", 10 ** 8, date(2022, 4, 27))
primer = Stanje(
    kuverte = [
        Kuverta("hrana", [
            od_babice,
            iz_neba
        ])
    ],
    racuni = [
        Racun("gotovina", [
            od_babice
        ]),
        Racun("kriptovalute", [
            iz_neba
        ])
    ]
)