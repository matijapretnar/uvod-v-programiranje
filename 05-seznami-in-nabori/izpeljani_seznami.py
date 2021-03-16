def sodi_elementi(sez):
    sodi = []
    for x in sez:
        if x % 2 == 0:
            sodi.append(x)
    return sodi


def kvadrati_elementov(sez):
    kvadrati = []
    for x in sez:
        kvadrati.append(x ** 2)
    return kvadrati


def kvadrati_elementov(sez):
    return [x ** 2 for x in sez]


def sodi_elementi(sez):
    return [x for x in sez if x % 2 == 0]
