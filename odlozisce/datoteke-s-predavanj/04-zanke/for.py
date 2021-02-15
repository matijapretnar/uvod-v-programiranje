def vsota_elementov(seznam):
    vsota = 0
    for x in seznam:
        vsota += x
    return vsota

def stevilo_elementov(seznam):
    stevilo = 0
    for x in seznam:
        stevilo += 1
    return stevilo

def stevilo_sodih_elementov(seznam):
    stevilo = 0
    for x in seznam:
        if x % 2 == 0:
            stevilo += 1
    return stevilo
