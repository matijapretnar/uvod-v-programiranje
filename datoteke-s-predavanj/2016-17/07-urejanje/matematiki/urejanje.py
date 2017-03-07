def uredi_z_mehurcki(seznam):
    '''Na mestu uredi dani seznam.'''
    for obhod in range(1, len(seznam)):
        for prvi in range(0, len(seznam) - obhod - 1):
            if seznam[prvi] > seznam[prvi + 1]:
                seznam[prvi], seznam[prvi + 1] = seznam[prvi + 1], seznam[prvi]

def uredi_z_zlivanjem(seznam, zac=0, kon=None):
    if kon is None:
        kon = len(seznam)
    if kon - zac <= 1:
        return
    else:
        sre = (zac + kon) // 2
        uredi_z_zlivanjem(seznam, zac, sre)
        uredi_z_zlivanjem(seznam, sre, kon)
        zlij_na_mestu(seznam, zac, sre, kon)


def zlij_na_mestu(seznam, zac, sre, kon):
    zliti_seznam = (kon - zac) * [None]
    levi, desni, cilj = zac, sre, 0
    while levi < sre or desni < kon:
        if levi == sre:
            zliti_seznam[cilj] = seznam[desni]
            desni += 1
        elif desni == kon:
            zliti_seznam[cilj] = seznam[levi]
            levi += 1
        elif seznam[levi] <= seznam[desni]:
            zliti_seznam[cilj] = seznam[levi]
            levi += 1
        else:
            assert seznam[levi] > seznam[desni]
            zliti_seznam[cilj] = seznam[desni]
            desni += 1
        cilj += 1
    seznam[zac:kon] = zliti_seznam


besede = ['bila', 'je', 'huda', 'mravljica', 'šest', 'črnih', 'nog', 'je', 'imela']
osebe = [('Ivana', 'Kobilica'), ('Valentin', 'Vodnik'), ('France', 'Prešeren'), ('France', 'Bevk')]
