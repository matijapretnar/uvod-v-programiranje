def en_dva_tri(x=0):
    yield x + 1
    yield x + 2
    yield x + 3


def seznam_zaporednih_stevil(n):
    vsa_stevila = []
    i = 1
    while i <= n:
        vsa_stevila.append(i)
        i += 1
    return vsa_stevila


def generator_zaporednih_stevil(n):
    i = 1
    while i <= n:
        yield i
        i += 1


def neumno_sestej(n):
    vsota = 0
    for stevilo in seznam_zaporednih_stevil(n):
        vsota += stevilo
    return vsota

def malo_manj_neumno_sestej(n):
    vsota = 0
    for stevilo in generator_zaporednih_stevil(n):
        vsota += stevilo
    return vsota
