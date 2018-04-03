def yoda(niz):
    besede = niz.split()
    zadnja_beseda = besede[-1]
    prve_besede = besede[:-1]
    locilo = zadnja_beseda[-1]
    obrnjene_besede = [zadnja_beseda[:-1]] + prve_besede
    obrnjeni_niz = ' '.join(obrnjene_besede)
    return obrnjeni_niz.capitalize() + locilo