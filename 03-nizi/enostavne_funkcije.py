def srednja_crka(niz):
    dolzina = len(niz)
    indeks_srednje_crke = dolzina // 2
    return niz[indeks_srednje_crke]

def je_samoglasnik(niz):
    # Ne pišimo takole, ker deluje nenavadno
    # return niz == 'a' or 'e' or 'i' or 'o' or 'u' or 'A' or 'E' or 'I' or 'O' or 'U'

    # Deluje pravilno, ampak je malo dolgovezno
    # return (
    #     niz == 'a'
    #     or niz == 'e'
    #     or niz == 'i'
    #     or niz == 'o'
    #     or niz == 'u'
    #     or niz == 'A'
    #     or niz == 'E'
    #     or niz == 'I'
    #     or niz == 'O'
    #     or niz == 'U'
    # )

    # Ne pišimo if ...: return True else: return False
    # if niz in 'aeiouAEIOU':
    #     return True
    # else:
    #     return False

    # Tudi tega ne delamo
    # if len(niz) == 1:
    #     return niz in 'aeiouAEIOU'
    # else:
    #     return False

    return len(niz) == 1 and niz in 'aeiouAEIOU'

def ni_samoglasnik(niz):
    # return not je_samoglasnik(niz)

    return len(niz) != 1 or niz not in 'aeiouAEIOU'

def stevilo_samoglasnikov(niz):
    if niz == '':
        return 0
    elif je_samoglasnik(niz[0]):
        return 1 + stevilo_samoglasnikov(niz[1:])
    else:
        return stevilo_samoglasnikov(niz[1:])

def stevilo_samoglasnikov(niz, i, j):
    """Prešteje število samoglasnikov v niz od i-tega do (j-1)-tega znaka"""
    if i >= j:
        return 0
    elif je_samoglasnik(niz[i]):
        return 1 + stevilo_samoglasnikov(niz, i + 1, j)
    else:
        return stevilo_samoglasnikov(niz, i + 1, j)

def samoglasnike_zamenjaj_z_vprasaji(niz):
    if niz == '':
        return ''
    elif je_samoglasnik(niz[0]):
        return '?' + samoglasnike_zamenjaj_z_vprasaji(niz[1:])
    else:
        return niz[0] + samoglasnike_zamenjaj_z_vprasaji(niz[1:])

def kaksno_je_vreme(stopinje):
    if stopinje < 0:
        # return "Danes je pa mrzlo. Je kar " + str(-stopinje) + " stopinj pod ničlo."
        return f"Danes je pa mrzlo. Je kar {-stopinje} stopinj pod ničlo."
    else:
        return "Je kar toplo."

# p q  p OR q   p AND q
# F F    F         F
# F T    T         F
# T F    T         F
# T T    T         T

