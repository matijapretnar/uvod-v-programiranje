import os


def izpisi_imenik(pot, zamik=0):
    print(zamik * " " + os.path.basename(os.path.abspath(pot)))
    for ime_datoteke in sorted(os.listdir(pot)):
        polna_pot = os.path.join(pot, ime_datoteke)
        if ime_datoteke.startswith("."):
            continue
        elif os.path.isdir(polna_pot):
            izpisi_imenik(polna_pot, zamik=zamik+2)
        else:
            print(zamik * " " + "- " + ime_datoteke)

izpisi_imenik("..")