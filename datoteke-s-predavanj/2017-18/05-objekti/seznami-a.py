def vsi_sodi_elementi(seznam):
    sodi = []
    for x in seznam:
        if x % 2 == 0:
            sodi = sodi.append(x)
    return sodi

def delne_vsote(seznam):
    vsote = []
    trenutna_delna_vsota = 0
    for x in seznam:
        # print(vsote, trenutna_delna_vsota)
        trenutna_delna_vsota += x
        vsote.append(trenutna_delna_vsota)
    return vsote

def delne_vsote_bolj_pocasi(seznam):
    vsote = []
    for i in range(len(seznam)):
        vsote.append(sum(seznam[:i + 1]))
    return vsote
