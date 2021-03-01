def prestej_samoglasnike(niz):
    if niz == "":
        return 0
    preostanek_niza = niz[1:]
    samoglasniki_v_preostanku = prestej_samoglasnike(preostanek_niza)
    if niz[0].lower() in "aeiou":
        return samoglasniki_v_preostanku + 1
    else:
        return samoglasniki_v_preostanku
