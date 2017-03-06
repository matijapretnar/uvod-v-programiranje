import random

class Bakterija:
    '''
    Razred, ki predstavlja bakterije.
    Atributi objektov so:
    - starost (število minut)
    - DNK (genski zapis)
    '''

    def __init__(self, starost, dnk):
        self.starost = starost
        self.dnk = dnk
        starost += 10

    def __repr__(self):
        return 'Bakterija({}, {!r})'.format(self.starost, self.dnk)

    def __str__(self):
        return 'Bakterija, ki je stara {} minut in ima DNK: {}'.format(
            self.starost, self.dnk
        )

    def __truediv__(self, n):
        nove_bakterije = []
        for _ in range(n):
            nova_starost = self.starost + 1
            novi_dnk = self.dnk
            pobrisi = random.randint(0, len(novi_dnk) - 1)
            novi_dnk = novi_dnk[:pobrisi] + novi_dnk[pobrisi + 1:]
            nove_bakterije.append(Bakterija(nova_starost, novi_dnk))
        return nove_bakterije



    def postaraj(self, minute=1):
        self.starost += minute


class Ulomek:

    def __init__(self, stevec, imenovalec=1, vzdevek='ulomči'):
        self.stevec = stevec
        self.imenovalec = imenovalec
        self.vzdevek = vzdevek