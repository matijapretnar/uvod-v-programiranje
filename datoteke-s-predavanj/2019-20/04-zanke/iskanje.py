# SLABA REKURZIVNA
def poisci(x, seznam):
    if len(seznam) == 0:
        return False
    else:
        sredina = len(seznam) // 2
        if x == seznam[sredina]:
            return True
        elif x < seznam[sredina]:
            return poisci(x, seznam[:sredina])
        else:
            return poisci(x, seznam[sredina + 1:])

# SLABA Z ZANKAMI
def poisci(x, seznam):
    while len(seznam) > 0:
        sredina = len(seznam) // 2
        if x == seznam[sredina]:
            return True
        elif x < seznam[sredina]:
            seznam = seznam[:sredina]
        else:
            seznam = seznam[sredina + 1:]
    return False

# DOBRA Z ZANKAMI
def poisci(x, seznam):
    od = 0
    do = len(seznam)
    while od < do:
        sredina = (od + do) // 2
        if x == seznam[sredina]:
            return True
        elif x < seznam[sredina]:
            do = sredina
        else:
            od = sredina + 1
    return False

poisci(12, [-10, -5, 1, 3, 5, 10, 13, 20, 22, 25])
