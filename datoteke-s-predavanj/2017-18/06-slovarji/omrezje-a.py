knjiga_obrazov = {
    'Anka': {'Bogomir', 'Cvetka'},
    'Bogomir': {'Cvetka', 'Dragomir'},
    'Cvetka': {'Anka'},
    'Dragomir': {'Anka', 'Cvetka'},
}

def priporoci_prijatelja(omrezje, oseba):
    priporocila = set()
    for prijatelj in omrezje[oseba]:
        prijatelji_prijatelja = omrezje[prijatelj]
        priporocila |= prijatelji_prijatelja
    return priporocila - omrezje[oseba] - {oseba}
