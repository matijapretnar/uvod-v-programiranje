def obrni_na_glavo(niz):
    obrnjen = ''
    for znak in niz:
        obrnjen = znak + obrnjen
    return obrnjen

obrni_na_glavo('Perica reže raci rep')
