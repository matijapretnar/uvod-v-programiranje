import random



def racunaj_priblizke_pi():
    stevilo_vseh, stevilo_v_krogu = 0, 0

    while True:
        x, y = random.random(), random.random()
        stevilo_vseh += 1
        if x ** 2 + y ** 2 <= 1:
            stevilo_v_krogu += 1
            print(4 * stevilo_v_krogu / stevilo_vseh)


import math

def meci_kocke(iskano_stevilo, ustavitev, stevilo_kock):
    skupaj_dosezene_tocke = 0
    while skupaj_dosezene_tocke < ustavitev:
        # print('Do zdaj sem vrgel za {}, ne bom se še ustavil'.format(skupaj_dosezene_tocke))
        for _ in range(stevilo_kock):
            met = random.randint(1, 6)
            # print('Vrgel sem {}'.format(met))
            skupaj_dosezene_tocke += met
    # print('Končam pri {}'.format(skupaj_dosezene_tocke))
    if skupaj_dosezene_tocke <= iskano_stevilo:
        return 100 - math.sin((iskano_stevilo - skupaj_dosezene_tocke)) ** 2
    else:
        return 0


def oceni_strategijo(iskano_stevilo, ustavitev, stevilo_kock, stevilo_poskusov=1000):
    skupna_nagrada = 0
    for _ in range(stevilo_poskusov):
        skupna_nagrada += meci_kocke(iskano_stevilo, ustavitev, stevilo_kock)
    return skupna_nagrada / stevilo_poskusov


def prikazi_strategije(iskano_stevilo, stevilo_kock):
    for ustavitev in range(iskano_stevilo + 1):
        nagrada = oceni_strategijo(iskano_stevilo, ustavitev, stevilo_kock)
        print('{}: {}'.format(ustavitev, nagrada))
