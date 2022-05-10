from dataclasses import dataclass
from datetime import date
import json
from typing import List


@dataclass
class Transakcija:
    opis: str
    znesek: float
    datum: date

    def v_slovar(self):
        return {
            "opis": self.opis,
            "znesek": self.znesek,
            "datum": self.datum.isoformat(),
        }

    @classmethod
    def iz_slovarja(cls, slovar):
        return cls(
            opis=slovar["opis"],
            znesek=slovar["znesek"],
            datum=date.fromisoformat(slovar["datum"]),
        )


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

    def v_slovar(self):
        return {
            "ime": self.ime,
            "transakcije": [transakcija.v_slovar() for transakcija in self.transakcije],
        }

    @classmethod
    def iz_slovarja(cls, slovar):
        return cls(
            ime=slovar["ime"],
            transakcije=[Transakcija.iz_slovarja(sl) for sl in slovar["transakcije"]],
        )


class Kuverta(ZbirkaTransakcij):
    pass


class Racun(ZbirkaTransakcij):
    pass


@dataclass
class Proracun:
    kuverte: List[Kuverta]
    racuni: List[Racun]

    def v_slovar(self):
        return {
            "kuverte": [kuverta.v_slovar() for kuverta in self.kuverte],
            "racuni": [racun.v_slovar() for racun in self.racuni],
        }

    def v_datoteko(self, ime_datoteke):
        with open(ime_datoteke, "w") as f:
            json.dump(self.v_slovar(), f, ensure_ascii=False, indent=4)

    @classmethod
    def iz_slovarja(cls, slovar):
        return cls(
            kuverte=[Kuverta.iz_slovarja(sl) for sl in slovar["kuverte"]],
            racuni=[Racun.iz_slovarja(sl) for sl in slovar["racuni"]],
        )

    @classmethod
    def iz_datoteke(cls, ime_datoteke):
        with open(ime_datoteke) as f:
            return cls.iz_slovarja(json.load(f))


od_babice = Transakcija("babica za desetko pri UVP", 100, date(2022, 4, 26))
iz_neba = Transakcija("priletelo iz neba", 10**8, date(2022, 4, 27))
primer_proracuna = Proracun(
    kuverte=[Kuverta("hrana", [od_babice, iz_neba])],
    racuni=[Racun("gotovina", [od_babice]), Racun("kriptovalute", [iz_neba])],
)
