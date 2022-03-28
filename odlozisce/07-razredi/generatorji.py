def vrni_seznam_stevk(stevilo):
    seznam_stevk = []
    while stevilo > 0:
        seznam_stevk.append(stevilo % 10)
        stevilo //= 10
    return seznam_stevk


def vrni_vsako_stevko(stevilo):
    while stevilo > 0:
        return stevilo % 10
        stevilo //= 10


def izpisi_vsako_stevko(stevilo):
    while stevilo > 0:
        print(stevilo % 10)
        stevilo //= 10


def generiraj_vsako_stevko(stevilo):
    while stevilo > 0:
        yield stevilo % 10
        stevilo //= 10
