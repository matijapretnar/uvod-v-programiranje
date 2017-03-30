def pri_katerem_clenu_harmonicna_vrsta_preseze(x):
    k = 1
    vsota = 0
    while vsota <= x:
        vsota = vsota + 1 / k
        k = k + 1
    return k - 1

def ugani_besedo(iskana_beseda):
    stevilo_poskusov = 1
    while True:
        vnesena_beseda = input('Kaj misliš, da je moja beseda? ')
        if vnesena_beseda == iskana_beseda:
            print('Bravo!')
            return stevilo_poskusov
        else:
            print('Ne, ni!')
            stevilo_poskusov += 1
    
