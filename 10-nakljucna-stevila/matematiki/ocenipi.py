import random

def oceni_pi(stevilo_poskusov):
    v_krogu = 0
    for _ in range(stevilo_poskusov):
        x, y = random.random(), random.random()
        if x ** 2 + y ** 2 <= 1:
            v_krogu += 1
    return 4 * v_krogu / stevilo_poskusov


def oceni_eno_kocko(stevilo_poskusov):
    pogostosti = {}
    for _ in range(stevilo_poskusov):
        met = random.randint(1, 6)
        pogostosti[met] = pogostosti.get(met, 0) + 1
    return {met: pogostost / stevilo_poskusov for met, pogostost in pogostosti.items()}


def oceni_dve_kocki(stevilo_poskusov):
    pogostosti = {}
    for _ in range(stevilo_poskusov):
        met = random.randint(1, 6) + random.randint(1, 6)
        pogostosti[met] = pogostosti.get(met, 0) + 1
    return {met: pogostost / stevilo_poskusov for met, pogostost in pogostosti.items()}


def oceni_max_tri_kocke(stevilo_poskusov):
    pogostosti = {}
    for _ in range(stevilo_poskusov):
        met = max(random.randint(1, 6), random.randint(1, 6), random.randint(1, 6))
        pogostosti[met] = pogostosti.get(met, 0) + 1
    return {met: pogostost / stevilo_poskusov for met, pogostost in pogostosti.items()}