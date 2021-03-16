from functools import cache
from typing import List

Veriga = List[bool]  # seznam binarnih vrednosti, ki povedo, ali se znak na danem mestu pojavi v končnem nizu
Pot = List[str]  # seznam korakov, ki nas pripelje od prve do zadnje besede


def stakni(pot1: Pot, pot2: Pot) -> Pot:
    return pot1 + pot2


def dolzina_poti(pot: Pot) -> int:
    return len(pot)


def krajse_od(poti1: List[Pot], poti2: List[Pot]) -> List[Pot]:
    if dolzina_poti(poti1[0]) < dolzina_poti(poti2[0]):
        return poti1
    elif dolzina_poti(poti1[0]) > dolzina_poti(poti2[0]):
        return poti2
    else:
        return poti1 + poti2


def naslednje_moznosti(veriga: Veriga) -> List[Veriga]:
    """
    Vrne vse možne spremembe False -> True, ki jih na dani verigi lahko naredimo
    :param veriga: začetna veriga
    :type veriga: Veriga
    :return: seznam spremenjenih verig
    :rtype: List[Veriga]
    """
    naslednje = []
    for x in range(len(veriga)):
        if veriga[x]:
            continue
        naslednje.append(veriga[:])  # kopija, ker jo želimo popravljati neodvisno od drugih
        naslednje[-1][x] = True
    return naslednje


def generiraj_do_konca(veriga: Veriga) -> List[List[Veriga]]:
    """
    Pripravi vse načine, na katere lahko dano verigo spremenimo v verigo, kjer so vse vrednosti True
    :param veriga: začetna veriga
    :type veriga: Veriga
    :return: seznam vseh poti, po katerih lahko spremenimo vse vrednosti v verigi v True
    :rtype: List[List[Veriga]]
    """
    if all(veriga):
        return [[veriga]]

    vse_verige = []

    for moznost in naslednje_moznosti(veriga):
        vse_verige.extend([[veriga] + naslednja for naslednja in generiraj_do_konca(moznost)])

    return vse_verige


def okrni(beseda: str, veriga: Veriga) -> str:
    """
    Ohrani znake iz besede le na tistih mestih, kjer ima veriga vrednost True
    :param beseda: začetna beseda
    :type beseda: str
    :param veriga: Veriga, ki pove katere znake naj ohranimo
    :type veriga: Veriga
    :return: okrnjena beseda
    :rtype: str
    """
    return "".join(crka for crka, prisotna in zip(beseda, veriga) if prisotna)


def pot_od_prazne_besede(beseda: str) -> List[Pot]:
    zacetna = [False for _ in range(len(beseda))]
    vse_verige = generiraj_do_konca(zacetna)
    besede = [[okrni(beseda, veriga) for veriga in pot] for pot in vse_verige]
    return besede


def pot_do_prazne_besede(beseda: str) -> List[Pot]:
    return [pot[::-1] for pot in pot_od_prazne_besede(beseda)]


def pot_dolzine_ena(beseda: str) -> Pot:
    return [beseda]


def dodaj_znak_vsakemu_koraku(znak: str, pot: Pot) -> Pot:
    return [znak + korak for korak in pot]


@cache
def vse_najkrajse_poti(beseda1: str, beseda2: str) -> List[Pot]:
    if beseda1 == "":
        # lahko jih je več
        return pot_od_prazne_besede(beseda2)
    elif beseda2 == "":
        # lahko jih je več
        return pot_do_prazne_besede(beseda1)
    elif beseda1[0] == beseda2[0]:
        # Xabc ~> ... ~> Xxyz
        # kjer je abc ~> ... ~> xyz
        poti_med_repoma = vse_najkrajse_poti(beseda1[1:], beseda2[1:])
        return [dodaj_znak_vsakemu_koraku(beseda1[0], pot) for pot in poti_med_repoma]
    else:
        # Xabc ~> ... ~> Ydef

        # X zamenjamo z Y
        # Xabc ~> Yabc ~> Y... ~> Ydef
        poti_med_repoma = vse_najkrajse_poti(beseda1[1:], beseda2[1:])
        zamenjamo = [
            stakni(pot_dolzine_ena(beseda1), dodaj_znak_vsakemu_koraku(beseda2[0], pot))
            for pot in poti_med_repoma
        ]

        # X pobrišemo
        # Xabc ~> abc ~> ... ~> Ydef
        pobrisemo = [
            stakni(pot_dolzine_ena(beseda1), pot)
            for pot in vse_najkrajse_poti(beseda1[1:], beseda2)
        ]

        # Y dodamo
        # Xabc ~> ... ~> def ~> Ydef
        dodamo = [
            stakni(pot, pot_dolzine_ena(beseda2))
            for pot in vse_najkrajse_poti(beseda1, beseda2[1:])
        ]

        return krajse_od(zamenjamo, krajse_od(pobrisemo, dodamo))
        # return min([zamenjamo, pobrisemo, dodamo], key=len)
