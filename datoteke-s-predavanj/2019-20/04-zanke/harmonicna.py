def cleni_harmonicne_vrste(meja):
    """Vrne najmanjši n, da velja
        1 + 1/2 + 1/3 + ... + 1/n > meja
    """
    n = 0
    vsota = 0
    while vsota <= meja:
        n += 1
        vsota += 1 / n
    return n
