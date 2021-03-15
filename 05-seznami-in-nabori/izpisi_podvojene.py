def izpisi_podvojene(sez):
    for i in range(len(sez)):
        x = sez[i]
        if x in sez[:i]:
            print(x)

izpisi_podvojene([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])
print()

def izpisi_podvojene(sez):
    i = 0
    for x in sez:
        if x in sez[:i]:
            print(x)
        i += 1

izpisi_podvojene([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])
print()

def izpisi_podvojene(sez):
    for i, x in enumerate(sez):
        if x in sez[:i]:
            print(x)

izpisi_podvojene([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])
print()


def izpisi_podvojene(sez):
    ze_videni = []
    for x in sez:
        if x in ze_videni:
            print(x)
        else:
            ze_videni += [x]

izpisi_podvojene([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])
print()

def izpisi_podvojene(sez):
    ze_videni = []
    for x in sez:
        if x in ze_videni:
            print(x)
        else:
            ze_videni.append(x)

izpisi_podvojene([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])
print()