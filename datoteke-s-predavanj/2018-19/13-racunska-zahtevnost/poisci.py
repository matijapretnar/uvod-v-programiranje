import stopaj

def poisci_nas(seznam):
    n = len(seznam) // 2
    for x in seznam:
        if x == n:
            return True
    return False

def poisci_v_urejenem(seznam):
    n = len(seznam) // 2
    for x in seznam:
        if x == n:
            return True
        elif x > n:
            return False
    return False

def bisekcija(seznam, x, od, do):
    '''Ali seznam[od:do] vsebuje x'''
    if od == do:
        return False
    else:
        i = (od + do) // 2
        if seznam[i] == x:
            return True
        elif seznam[i] > x:
            return bisekcija(seznam, x, od, i)
        elif seznam[i] < x:
            return bisekcija(seznam, x, i + 1, do)
            

def poisci_z_bisekcijo(seznam):
    n = len(seznam) // 2
    return bisekcija(seznam, n, 0, len(seznam))

def poisci_vgrajen(seznam):
    return len(seznam) in seznam


stopaj.izmeri_case_poskusov(
    [stopaj.nakljucen_narascajoc_seznam(n) for n in range(1000, 100000, 5000)],
    [poisci_nas, poisci_v_urejenem, poisci_vgrajen, poisci_z_bisekcijo]
)