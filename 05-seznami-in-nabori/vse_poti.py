from functools import cache


def stakni(pot1, pot2):
    return pot1 + pot2


def dolzina_poti(pot):
    return len(pot)


def krajse_od(poti1, poti2):
    if dolzina_poti(poti1[0]) < dolzina_poti(poti2[0]):
        return poti1
    elif dolzina_poti(poti1[0]) > dolzina_poti(poti2[0]):
        return poti2
    else:
        return poti1 + poti2


def pot_od_prazne_besede(beseda):
    return [beseda[:i] for i in range(len(beseda) + 1)]


def pot_do_prazne_besede(beseda):
    return pot_od_prazne_besede(beseda)[::-1]


def pot_dolzine_ena(beseda):
    return [beseda]


def dodaj_znak_vsakemu_koraku(znak, pot):
    return [znak + korak for korak in pot]


@cache
def vse_najkrajse_poti(beseda1, beseda2):
    if beseda1 == "":
        # lahko jih je več
        return [pot_od_prazne_besede(beseda2)]
    elif beseda2 == "":
        # lahko jih je več
        return [pot_do_prazne_besede(beseda1)]
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
