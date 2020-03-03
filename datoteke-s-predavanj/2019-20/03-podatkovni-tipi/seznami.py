def povprecje(seznam):
    if seznam:
        return sum(seznam) / len(seznam)
    else:
        return None

def razpon(seznam):
    return max(seznam) - min(seznam)

def vsebuje_sodega(seznam):
    if len(seznam) == 0:
        return False
    elif seznam[0] % 2 == 0:
        return True
    else:
        return vsebuje_sodega(seznam[1:])
