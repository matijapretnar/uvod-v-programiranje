class Slovar:
    def __init__(self, stevilo_skatel=8):
        self.stevilo_elementov = 0
        self.skatle = [[] for _ in range(stevilo_skatel)]

    def __str__(self):
        return str(self.skatle)

    def _indeks_skatle(self, k):
        return hash(k) % len(self.skatle)

    def _preuredi(self):
        vecji_slovar = Slovar(stevilo_skatel=2 * len(self.skatle))
        for skatla in self.skatle:
            for k, v in skatla:
                vecji_slovar[k] = v
        self.skatle = vecji_slovar.skatle

    def __setitem__(self, k, v):
        i = self._indeks_skatle(k)
        self.skatle[i].append((k, v))
        self.stevilo_elementov += 1
        if self.stevilo_elementov > 2 * len(self.skatle):
            self._preuredi()

    def __getitem__(self, k):
        i = self._indeks_skatle(k)
        for l, v in self.skatle[i]:
            if l == k:
                return v

    def __iter__(self):
        for skatla in self.skatle:
            for k, v in skatla:
                yield (k, v)
    
    def __len__(self):
        return self.stevilo_elementov


s = Slovar()
s[1] = 10
s[9] = 20
s["abc"] = 5
