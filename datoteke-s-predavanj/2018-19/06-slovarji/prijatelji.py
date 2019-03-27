knjiga_obrazov = {
    'Anka': {'Bogomir', 'Cvetka'},
    'Bogomir': {'Cvetka', 'Dragomir'},
    'Cvetka': {'Anka'},
    'Dragomir': {'Anka', 'Cvetka'},
}

def priporoci(omrezje, oseba):
    stari_prijatelji = omrezje[oseba]
    novi_prijatelji = set()
    for prijatelj in stari_prijatelji:
        prijatelji_prijatelja = omrezje[prijatelj]
        novi_prijatelji |= prijatelji_prijatelja
    return novi_prijatelji - stari_prijatelji - {oseba}

print(priporoci(knjiga_obrazov, 'Bogomir'))
print(priporoci(knjiga_obrazov, 'Cvetka'))