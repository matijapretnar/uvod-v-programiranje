import json

class Proracun:
    def __init__(self):
        self.racuni = []
        self.kuverte = []
        self.prelivi = []

    def nov_racun(self, ime):
        for racun in self.racuni:
            if racun.ime == ime:
                raise ValueError('Račun s tem imenom že obstaja!')
        nov = Racun(ime, self)
        self.racuni.append(nov)
        return nov

    def nova_kuverta(self, ime, razporeditev=0):
        for kuverta in self.kuverte:
            if kuverta.ime == ime:
                raise ValueError('Kuverta s tem imenom že obstaja!')
        nova = Kuverta(ime, razporeditev, self)
        self.kuverte.append(nova)
        return nova
    
    def odstrani_kuverto(self, kuverta):
        self._preveri_kuverto(kuverta)
        for preliv in kuverta.prelivi():
            preliv.kuverta = None
        self.kuverte.remove(kuverta)
    
    def nov_preliv(self, znesek, datum, opis, racun, kuverta):
        self._preveri_kuverto(kuverta)
        self._preveri_racun(racun)
        nov = Preliv(znesek, datum, opis, racun, kuverta)
        self.prelivi.append(nov)
        return nov

    def _preveri_racun(self, racun):
        if racun.proracun != self:
            raise ValueError(f'Račun {racun} ne spada v ta proračun!')

    def _preveri_kuverto(self, kuverta):
        if kuverta is not None and kuverta.proracun != self:
            raise ValueError(f'Kuverta {kuverta} ne spada v ta proračun!')

    def nerazporejena_sredstva(self):
        vrednost_nerazporejenih_prelivov = sum(preliv.znesek for preliv in self.prelivi if preliv.kuverta is None)
        razporeditev_v_kuverte = sum(kuverta.razporeditev for kuverta in self.kuverte)
        return vrednost_nerazporejenih_prelivov - razporeditev_v_kuverte

    def premakni_denar(self, kuverta1, kuverta2, znesek):
        self._preveri_kuverto(kuverta1)
        self._preveri_kuverto(kuverta2)
        if kuverta1 is not None:
            kuverta1.razporeditev -= znesek
        if kuverta2 is not None:
            kuverta2.razporeditev += znesek

    def _slovar_s_stanjem(self):
        return {
            'racuni': [{
                'ime': racun.ime,
            } for racun in self.racuni],
            'kuverte': [{
                'ime': kuverta.ime,
                'razporeditev': kuverta.razporeditev,
            } for kuverta in self.kuverte],
            'prelivi': [{
                'znesek': preliv.znesek,
                'datum': str(preliv.datum),
                'opis': preliv.opis,
                'racun': preliv.racun.ime,
                'kuverta': None if preliv.kuverta is None else preliv.kuverta.ime,
            } for preliv in self.prelivi],
        }
    
    def shrani_stanje(self, ime_datoteke):
        with open(ime_datoteke, 'w') as datoteka:
            json.dump(self._slovar_s_stanjem(), datoteka, ensure_ascii=False, indent=4)
    
    @staticmethod
    def nalozi_stanje(ime_datoteke):
        with open(ime_datoteke) as datoteka:
            slovar_s_stanjem = json.load(datoteka)
        racuni_po_imenu = {}
        kuverte_po_imenu = {None: None}
        for racun in slovar_s_stanjem['racuni']:
            nov_racun = proracun.nov_racun(racun['ime'])
            racuni_po_imenu[racun['ime']] = nov_racun
        for kuverta in slovar_s_stanjem['kuverte']:
            nova_kuverta = proracun.nova_kuverta(kuverta['ime'], kuverta['razporeditev'])
            kuverte_po_imenu[kuverta['ime']] = nova_kuverta
        for preliv in slovar_s_stanjem['prelivi']:
            proracun.nov_preliv(
                preliv['znesek'],
                preliv['datum'],
                preliv['opis'],
                racuni_po_imenu[preliv['racun']],
                kuverte_po_imenu[preliv['kuverta']],
            )
        return proracun


class Racun:
    def __init__(self, ime, proracun):
        self.ime = ime
        self.proracun = proracun

    def stanje(self):
        return sum([preliv.znesek for preliv in self.prelivi()])

    def prelivi(self):
        for preliv in self.proracun.prelivi:
            if preliv.racun == self:
                yield preliv


class Kuverta:
    def __init__(self, ime, razporeditev, proracun):
        self.ime = ime
        self.proracun = proracun
        self.razporeditev = razporeditev

    def prelivi(self):
        for preliv in self.proracun.prelivi:
            if preliv.kuverta == self:
                yield preliv

    def stanje(self):
        return self.razporeditev + sum([preliv.znesek for preliv in self.prelivi()])


class Preliv:
    def __init__(self, znesek, datum, opis, racun, kuverta):
        self.znesek = znesek
        self.datum = datum
        self.opis = opis
        self.racun = racun
        self.kuverta = kuverta
