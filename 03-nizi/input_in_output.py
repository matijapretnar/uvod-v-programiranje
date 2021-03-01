def odstevaj_do_nic(n):
    if n == 0:
        print("Booom!")
    else:
        print(n)
        odstevaj_do_nic(n - 1)


def lepo_pozdravi():
    print("Kako ti je pa ime?")
    ime = input()
    print("Pozdravljeni, " + ime)
    print("Ponovimo...")
    lepo_pozdravi()


def odstevaj():
    stevilka = input("Od kod bi rad odšteval? ")
    if stevilka.isnumeric():
        odstevaj_do_nic(int(stevilka))
    else:
        print("To pa ni številka! Poskusimo ponovno...")
        odstevaj()
