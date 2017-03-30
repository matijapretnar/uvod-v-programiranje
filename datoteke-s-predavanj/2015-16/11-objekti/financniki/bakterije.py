import random

class Bakterija:

    def __init__(self, dnk, starost=1):
        self.dnk = dnk
        self.starost = starost

    def postaraj_se(self, za_koliko=1):
        self.starost += za_koliko

    def mutiraj(self, verjetnost_mutacije=0.4):
        nov_dnk = ''
        for nukleotid in self.dnk:
            if random.random() < verjetnost_mutacije:
                nov_dnk += random.choice('ACGT')
            else:
                nov_dnk += nukleotid
        self.dnk = nov_dnk


    def __str__(self):
        return 'Bakterija z DNK: {}, stara {} sekund'.format(self.dnk, self.starost)

    def __repr__(self):
        return 'Bakterija(\'{}\', starost={})'.format(self.dnk, self.starost)

