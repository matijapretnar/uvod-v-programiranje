LOCILO = " ~> "


def stakni(niz1, niz2):
    return niz1 + LOCILO + niz2


def dolzina_poti(pot):
    return pot.count(LOCILO)


def krajsa_od(pot1, pot2):
    return pot1 if dolzina_poti(pot1) <= dolzina_poti(pot2) else pot2


def pot_od_prazne_besede(beseda):
    return "" if beseda == "" else stakni(pot_od_prazne_besede(beseda[1:]), beseda)


def pot_do_prazne_besede(beseda):
    return "" if beseda == "" else stakni(beseda, pot_do_prazne_besede(beseda[1:]))


def dodaj_znak_vsakemu_koraku(znak, pot):
    return znak + pot.replace(LOCILO, LOCILO + znak)


def najkrajsa_pot(beseda1, beseda2):
    if beseda1 == "":
        return pot_od_prazne_besede(beseda2)
    elif beseda2 == "":
        return pot_do_prazne_besede(beseda1)
    elif beseda1[0] == beseda2[0]:
        # Xabc ~> ... ~> Xxyz
        # kjer je abc ~> ... ~> xyz
        pot_med_repoma = najkrajsa_pot(beseda1[1:], beseda2[1:])
        return dodaj_znak_vsakemu_koraku(beseda1[0], pot_med_repoma)
    else:
        # Xabc ~> ... ~> Ydef
        # X zamenjamo z Y
        # Xabc ~> Yabc ~> Y... ~> Ydef
        pot_med_repoma = najkrajsa_pot(beseda1[1:], beseda2[1:])
        zamenjamo = stakni(
            beseda1, dodaj_znak_vsakemu_koraku(beseda2[0], pot_med_repoma)
        )
        # X pobrišemo
        # Xabc ~> abc ~> ... ~> Ydef
        pobrisemo = stakni(beseda1, najkrajsa_pot(beseda1[1:], beseda2))
        # Y dodamo
        # Xabc ~> ... ~> def ~> Ydef
        dodamo = stakni(najkrajsa_pot(beseda1, beseda2[1:]), beseda2)
        return krajsa_od(zamenjamo, krajsa_od(pobrisemo, dodamo))
