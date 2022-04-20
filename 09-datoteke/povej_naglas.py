with open("krst-pri-savici.txt", encoding="utf-8") as vhod:
    with open("KRST-PRI-SAVICI!TXT", "w", encoding="utf-8") as izhod:
        for vrstica in vhod:
            # izhod.write(vrstica.upper())
            print(vrstica.upper(), file=izhod, end="")
