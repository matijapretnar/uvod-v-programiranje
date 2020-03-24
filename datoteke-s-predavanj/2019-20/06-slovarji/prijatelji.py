knjiga_obrazov = {
    'Anka': {'Bogomir', 'Cvetka'},
    'Bogomir': {'Cvetka', 'Dragomir'},
    'Cvetka': {'Anka'},
    'Dragomir': {'Anka', 'Cvetka'},
}

def priporoci(omrezje, oseba):
    prijatelji = omrezje[oseba]
    prijatelji_prijateljev = set()
    for prijatelj in prijatelji:
        prijatelji_prijatelja = omrezje[prijatelj]
        prijatelji_prijateljev.update(prijatelji_prijatelja)
    return prijatelji_prijateljev - prijatelji - {oseba} 

print(priporoci(knjiga_obrazov, 'Bogomir'))
print(priporoci(knjiga_obrazov, 'Cvetka'))