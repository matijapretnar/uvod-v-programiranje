class AritmeticnoZaporedje:
    def __init__(self, zacetni_clen, razlika):
        self.zacetni_clen = zacetni_clen
        self.razlika = razlika

    def clen(self, i):
        """Vrne i-ti člen zaporedja"""
        return self.zacetni_clen + i * self.razlika

    def _vsota_od_zacetka(self, i):
        """Vrne vsoto a0 + a1 + ... + a_i-1"""
        # To razume še Gauss
        return (i - 1) * self.zacetni_clen + i * (i - 1) // 2 * self.razlika

    def vsota(self, i, j):
        """Vrne vsoto ai + a_i+1 + ... + a_j-1"""
        return self._vsota_od_zacetka(j) - self._vsota_od_zacetka(i)

    def __repr__(self):
        return f"AritmeticnoZaporedje({self.zacetni_clen}, {self.razlika})"

    def __str__(self):
        return f"{self.clen(0)}, {self.clen(1)}, {self.clen(2)}, ..."

    def __add__(self, other):
        return AritmeticnoZaporedje(
            self.zacetni_clen + other.zacetni_clen, self.razlika + other.razlika
        )

    def __eq__(self, other):
        return self.zacetni_clen == other.zacetni_clen and self.razlika == other.razlika

    def vsi_cleni(self):
        clen = self.zacetni_clen
        while True:
            yield clen
            clen += self.razlika
