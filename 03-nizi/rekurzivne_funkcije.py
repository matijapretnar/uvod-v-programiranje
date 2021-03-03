def prestej_samoglasnike(niz):
    if niz == "":
        return 0
    preostanek_niza = niz[1:]
    samoglasniki_v_preostanku = prestej_samoglasnike(preostanek_niza)
    if niz[0].lower() in "aeiou":
        return samoglasniki_v_preostanku + 1
    else:
        return samoglasniki_v_preostanku


# Še bolj učinkovita varianta, ki ne kopira nizev


def prestej_samoglasnike(niz, i=0):
    """Prešteje vse samoglasnike v nizu od indeksa i naprej"""
    if i >= len(niz):
        return 0
    elif niz[i].lower() in "aeiou":
        return 1 + prestej_samoglasnike(niz, i + 1)
    else:
        return prestej_samoglasnike(niz, i + 1)
