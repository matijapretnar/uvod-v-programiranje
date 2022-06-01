from dataclasses import dataclass
from datetime import date
import json
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


@dataclass
class Kuverta(ZbirkaTransakcij):
    razporejeno: float = 0

    @staticmethod
    def premakni_denar(iz_kuverte, v_kuverto, znesek):
        if iz_kuverte:
            iz_kuverte.razporejeno -= znesek
        if v_kuverto:
            v_kuverto.razporejeno += znesek

    def stanje(self):
        return self.razporejeno + super().stanje()


class Racun(ZbirkaTransakcij):
    pass


@dataclass
class Proracun:
    kuverte: List[Kuverta]
    racuni: List[Racun]

    def stanje(self):
        return sum(racun.stanje() for racun in self.racuni)

    def nerazporejena_sredstva(self):
        return self.stanje() - sum(kuverta.stanje() for kuverta in self.kuverte)

    def transakcije(self):
        for id_racuna, racun in enumerate(self.racuni):
            for transakcija in racun.transakcije:
                transakcija.racun = racun
                transakcija.id_racuna = id_racuna
                transakcija.kuverta = None
                transakcija.id_kuverte = None
        for id_kuverte, kuverta in enumerate(self.kuverte):
            for transakcija in kuverta.transakcije:
                transakcija.kuverta = kuverta
                transakcija.id_kuverte = id_kuverte
        for racun in self.racuni:
            yield from racun.transakcije

    def dodaj_kuverto(self, ime):
        kuverta = Kuverta(ime, [])
        self.kuverte.append(kuverta)

    def dodaj_racun(self, ime):
        racun = Racun(ime, [])
        self.racuni.append(racun)

    def dodaj_transakcijo(self, opis, znesek, datum, racun, kuverta):
        transakcija = Transakcija(opis, znesek, datum)
        racun.dodaj_transakcijo(transakcija)
        if kuverta:
            kuverta.dodaj_transakcijo(transakcija)

    def v_slovar(self):
        slovarji_transakcij = []
        for transakcija in self.transakcije():
            slovarji_transakcij.append(
                {
                    "opis": transakcija.opis,
                    "znesek": transakcija.znesek,
                    "datum": transakcija.datum.isoformat(),
                    "racun": transakcija.id_racuna,
                    "kuverta": transakcija.id_kuverte,
                }
            )

        return {
            "kuverte": [
                {"ime": kuverta.ime, "razporejeno": kuverta.razporejeno}
                for kuverta in self.kuverte
            ],
            "racuni": [{"ime": racun.ime} for racun in self.racuni],
            "transakcije": slovarji_transakcij,
        }

    @classmethod
    def iz_slovarja(cls, slovar):
        kuverte = [
            Kuverta(sl["ime"], [], sl["razporejeno"]) for sl in slovar["kuverte"]
        ]
        racuni = [Racun(sl["ime"], []) for sl in slovar["racuni"]]
        for sl in slovar["transakcije"]:
            transakcija = Transakcija(
                opis=sl["opis"],
                znesek=sl["znesek"],
                datum=date.fromisoformat(sl["datum"]),
            )
            if sl["kuverta"] is not None:
                kuverte[sl["kuverta"]].dodaj_transakcijo(transakcija)
            racuni[sl["racun"]].dodaj_transakcijo(transakcija)
        return cls(
            kuverte=kuverte,
            racuni=racuni,
        )


@dataclass
class Uporabnik:
    uporabnisko_ime: str
    zasifrirano_geslo: str
    proracun: Proracun

    @staticmethod
    def zasifriraj_geslo(geslo_v_cistopisu):
        return "XXX" + geslo_v_cistopisu[::-1] + "XXX"

    def ima_geslo(self, geslo_v_cistopisu):
        return self.zasifriraj_geslo(geslo_v_cistopisu) == self.zasifrirano_geslo
    
    def nastavi_novo_geslo(self, geslo_v_cistopisu):
        self.zasifrirano_geslo = self.zasifriraj_geslo(geslo_v_cistopisu)

    def v_slovar(self):
        return {
            "uporabnisko_ime": self.uporabnisko_ime,
            "zasifrirano_geslo": self.zasifrirano_geslo,
            "proracun": self.proracun.v_slovar(),
        }

    @classmethod
    def iz_slovarja(cls, slovar):
        return cls(
            uporabnisko_ime=slovar["uporabnisko_ime"],
            zasifrirano_geslo=slovar["zasifrirano_geslo"],
            proracun=Proracun.iz_slovarja(slovar["proracun"]),
        )


@dataclass
class VseSkupaj:
    uporabniki: List[Uporabnik]

    def poisci_uporabnika(self, uporabnisko_ime, geslo_v_cistopisu=None):
        for uporabnik in self.uporabniki:
            if uporabnik.uporabnisko_ime == uporabnisko_ime:
                if geslo_v_cistopisu is None or uporabnik.ima_geslo(geslo_v_cistopisu):
                    return uporabnik

    def v_slovar(self):
        return {
            "uporabniki": [uporabnik.v_slovar() for uporabnik in self.uporabniki],
        }

    @classmethod
    def iz_slovarja(cls, slovar):
        return cls(
            uporabniki=[Uporabnik.iz_slovarja(sl) for sl in slovar["uporabniki"]]
        )

    def v_datoteko(self, ime_datoteke):
        with open(ime_datoteke, "w") as f:
            json.dump(self.v_slovar(), f, ensure_ascii=False, indent=4)

    @classmethod
    def iz_datoteke(cls, ime_datoteke):
        with open(ime_datoteke) as f:
            return cls.iz_slovarja(json.load(f))


stipendija = Transakcija("štipendija", 220, date(2022, 5, 10))
najemnina = Transakcija("najemnina", -120, date(2022, 5, 1))
mesecna = Transakcija("mesečna", -25, date(2022, 5, 3))
bankomat_trr = Transakcija("bankomat", -50, date(2022, 5, 1))
bankomat_gotovina = Transakcija("bankomat", 50, date(2022, 5, 1))
primer_proracuna = Proracun(
    kuverte=[Kuverta("stroški", [najemnina, mesecna], 150), Kuverta("zabava", [], 0)],
    racuni=[
        Racun("gotovina", [mesecna, bankomat_gotovina]),
        Racun("TRR", [stipendija, najemnina, bankomat_trr]),
    ],
)
primer_vsega_skupaj = VseSkupaj(
    uporabniki=[
        Uporabnik(
            "matija",
            "geslo",
            proracun=primer_proracuna
        )
    ]
)
