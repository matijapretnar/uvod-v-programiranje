# Če imamo več kot en return, funkcija vrne prvo vrednost, saj
# se naslednji ukazi ne izvedejo.


def dva_returna(x):
    return 10 * x
    return 20 * x


# Če ni nič returnov, funkcija vrne posebno vrednost None
# Nanjo moramo biti pozorni, če rezultat funkcije uporabljamo
# še kje drugje, saj dobimo napako, ki omenja NoneType


def brez_returnov(x):
    10 * x


# Podobno funkcija vrne None, kadar napišemo return brez
# vrednosti, ki naj bi jo funkcija vrnila


def return_brez_vrednosti(x):
    2 * x
    return


# Spremenljivke, ki jih uporabljamo v funkciji so lokalne:
# funkcija ne spreminja spremenljivk, ki so definirane izven nje,
# prav tako pa njene spremenljivke po koncu izvajanja niso vidne.

a = 10


def f_ki_kao_prepise_a(x):
    a = 2 * x
    return a * a


# Po klicu funkcije bo a še vedno 10

# Funkcije lahko vseeno berejo poprej definirane spremenljivke


def f_ki_prebere_a(x):
    b = a * x
    return b * b


# Parametri so lahko neobvezni, če jim podamo privzeto vrednost


def koren(x, k=2):
    return x ** (1 / k)
