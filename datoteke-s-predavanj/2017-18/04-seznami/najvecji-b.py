def najvecji_element(seznam):
    if seznam:
        najvecji_do_zdaj = seznam[0]

        for x in seznam:
            if x > najvecji_do_zdaj:
                najvecji_do_zdaj = x

        return najvecji_do_zdaj


def najdaljsi_podseznam(seznami):
    if seznami:
        najdaljsi_do_zdaj = seznami[0]

        for seznam in seznami:
            if len(seznam) > len(najdaljsi_do_zdaj):
                najdaljsi_do_zdaj = seznam

        return najdaljsi_do_zdaj


def najvecja_vrednost(f, seznam):
    if seznam:
        najvecji_do_zdaj = seznam[0]
        najvecja_vrednost = f(seznam[0])

        for x in seznam:
            y = f(x)
            if y > najvecja_vrednost:
                najvecji_do_zdaj = x
                najvecja_vrednost = y

        return najvecji_do_zdaj


def najvecji_sodi_element(seznam):
    if seznam:
        najvecji_do_zdaj = None

        for x in seznam:
            print(x, najvecji_do_zdaj)
            if x % 2 == 0 and (najvecji_do_zdaj is None or x > najvecji_do_zdaj):
                najvecji_do_zdaj = x

        return najvecji_do_zdaj
