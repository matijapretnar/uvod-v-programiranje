import os

def ignoriraj(ime):
    return ime == "untracked" or ime[0] in [".", "_"]

def izpisi_vsebino_imenika(pot_imenika, zamik=0):
    for ime in sorted(os.listdir(pot_imenika)):
        polno_ime = os.path.join(pot_imenika, ime)
        print(zamik * ' ', ime)
        if os.path.isdir(polno_ime) and not ignoriraj(ime):
            izpisi_vsebino_imenika(polno_ime, zamik=zamik + 2)

izpisi_vsebino_imenika(".")
