def absolutna_vrednost(x):
    if x < 0:
        return -x
    else:
        return x


# Alternativna definicija
def absolutna_vrednost(x):
    if x < 0:
        absolutna = -x
    else:
        absolutna = x
    return absolutna


# Še ena definicija, ki pa je po nepotrebnem asimetrična
# def absolutna_vrednost(x):
#     if x < 0:
#         return -x
#     return x


def predznak(x):
    # Poskusili smo spodnje, vendar ne dela za 0
    # return x // absolutna_vrednost(x)
    if x == 0:
        return 0
    else:
        if x > 0:
            return 1
        else:
            return -1


# Še lepša, bolj simetrična varianta
def predznak(x):
    if x == 0:
        return 0
    elif x > 0:
        return 1
    else:
        return -1
