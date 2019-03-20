def seznam_kvadratov(seznam):
    kvadrati = []
    for x in seznam:
        kvadrati.append(x ** 2)
    return kvadrati

def dolzine_besed(seznam):
    dolzine = []
    for beseda in seznam:
        dolzine.append(len(beseda))
    return dolzine

def delne_vsote(seznam):
    vsote = []
    vsota = 0
    for x in seznam:
        vsota += x
        vsote.append(vsota)
    return vsote

def sodi_elementi(seznam):
    sodi = []
    for x in seznam:
        if x % 2 == 0:
            sodi.append(x)
        else:
            print('{0} pa ne maramo, ker ni sod'.format(x))
    return sodi
