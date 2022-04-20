from dataclasses import dataclass


@dataclass
class GeometrijskoZaporedje:
    zacetni_clen: int
    razmerje: int

    def clen(self, n):
        return self.zacetni_clen * self.razmerje**n

    def vsota(self, n):
        a = self.zacetni_clen
        qn = self.razmerje ** (n + 1) - 1
        q = self.razmerje - 1
        if isinstance(self.zacetni_clen, int) and isinstance(self.razmerje, int):
            return a * qn // q
        else:
            return a * qn / q

    def __str__(self):
        return f"{self.clen(0)}, {self.clen(1)}, {self.clen(2)}, …"

    def __mul__(self, other):
        return GeometrijskoZaporedje(
            self.zacetni_clen * other.zacetni_clen,
            self.razmerje * other.razmerje,
        )

@dataclass
class Ulomek:
    stevec: int
    imenovalec: int

    def __eq__(self, other):
        return self.stevec * other.imenovalec == self.imenovalec * other.stevec
