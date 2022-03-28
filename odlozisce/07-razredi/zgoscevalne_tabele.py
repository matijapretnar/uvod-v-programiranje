class Mnozica:
    def __init__(self, zacetni_elementi=[], n=8):
        self.st_elementov = 0
        self.skatle = [[] for _ in range(n)]
        for x in zacetni_elementi:
            self.dodaj(x)

    def _poisci_skatlo(self, n):
        skatle = self.skatle
        return skatle[n % len(skatle)]

    def _dodaj_brez_preurejanja(self, n):
        self.st_elementov += 1
        skatla = self._poisci_skatlo(n)
        if n not in skatla:
            skatla.append(n)


    def dodaj(self, n):
        self._dodaj_brez_preurejanja(n)
        if self.st_elementov > 2 * len(self.skatle):
            print(f"preurejam {self.st_elementov} {len(self.skatle)}")
            self._preuredi()
            print(f"končano")

    def _preuredi(self):
        nova_mnozica = Mnozica(n=2 * len(self.skatle))
        for n in self:
            nova_mnozica._dodaj_brez_preurejanja(n)
        self.skatle = nova_mnozica.skatle

    def __contains__(self, n):
        return n in self._poisci_skatlo(n)

    def __eq__(self, other):
        if self.st_elementov != other.st_elementov:
            return False
        for x in self:
            if x not in other:
                return False
        return True

    def __repr__(self):
        return f"Mnozica({list(self)})"

    def __str__(self):
        elementi_loceni_z_vejicami = ", ".join([str(x) for x in self])
        return f"{{{elementi_loceni_z_vejicami}}}"
    
    def __iter__(self):
        for skatla in self.skatle:
            for x in skatla:
                yield x





import random
m = Mnozica()
s = []
for x in range(20):
    y = random.randint(-1000 * x, 1000 * x)
    m.dodaj(y)
    # m.
    s.append(y)

n = Mnozica()
for x in s[::-1]:
    n.dodaj(x)
