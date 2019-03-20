def nicelna_matrika(n):
    return n * [n * [0]]

def nic_ali_ena(i, j):
    if i == j:
        return 1
    else:
        return 0

def identicna_matrika(n):
    matrika = []
    for i in range(n):
        vrstica = []
        for j in range(n):
            if i == j:
                vrstica.append(1)
            else:
                vrstica.append(0)
        matrika.append(vrstica)
    return matrika

identicna_matrika(4)