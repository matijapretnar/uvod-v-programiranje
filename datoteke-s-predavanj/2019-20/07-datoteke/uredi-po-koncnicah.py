from collections import Counter
import os


def prestej_koncnice(pot):
    stevec = Counter()
    for ime_datoteke in os.listdir(pot):
        polna_pot = os.path.join(pot, ime_datoteke)
        if os.path.isdir(polna_pot):
            stevec += prestej_koncnice(polna_pot)
        else:
            osnovno_ime, koncnica = os.path.splitext(polna_pot)
            if koncnica == '.pickle':
                print(polna_pot)
            stevec[koncnica] += 1
    return stevec

def izpisi_vsebino(pot, zamik=0, ignoriraj=['__pycache__']):
    for ime_datoteke in sorted(os.listdir(pot)):
        if ime_datoteke in ignoriraj:
            continue
        polna_pot = os.path.join(pot, ime_datoteke)
        print(zamik * ' ' + ime_datoteke)
        if os.path.isdir(polna_pot):
            izpisi_vsebino(polna_pot, zamik=(zamik + 4))

print(prestej_koncnice('.'))
izpisi_vsebino('datoteke-s-predavanj')
