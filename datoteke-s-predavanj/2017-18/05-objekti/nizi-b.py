def yoda(stavek):
    locilo = stavek[-1]
    besede = stavek[:-1].split()
    besede[0] = besede[0].lower()
    zadnja_beseda = besede[-1]
    preostale_besede = besede[:-1]
    obrnjene_besede = [zadnja_beseda] + preostale_besede
    obrnjene_besede[0] = obrnjene_besede[0].capitalize()
    obrnjen_stavek = ' '.join(obrnjene_besede) + locilo
    return obrnjen_stavek

print(yoda('Jaz sem Yoda!'))
print(yoda('Kdo si pa ti?'))