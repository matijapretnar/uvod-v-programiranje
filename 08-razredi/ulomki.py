def gcd(m, n):
    while n != 0:
        o = m % n
        m = n
        n = o
    return m


class Ulomek:
    def __init__(self, stevec, imenovalec):
        d = gcd(stevec, imenovalec)
        self.stevec = stevec // d
        self.imenovalec = imenovalec // d
    
    def __add__(self, other):
        return Ulomek(
            self.stevec * other.imenovalec + other.stevec * self.imenovalec,
            self.imenovalec * other.imenovalec
        )
    
    def __repr__(self):
        return f"Ulomek({self.stevec}, {self.imenovalec})"

    def __str__(self):
        return f"{self.stevec}/{self.imenovalec}"

    def __eq__(self, other):
        return self.stevec == other.stevec and self.imenovalec == other.imenovalec

a = Ulomek(1, 2)
b = Ulomek(1, 6)
