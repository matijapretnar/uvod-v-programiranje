def sodi_elementi(seznam):
    sodi = []
    for x in seznam:
        if x % 2 == 0:
            sodi.append(x)
    return sodi

print(sodi_elementi([10, -5, 2]))