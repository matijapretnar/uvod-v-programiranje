def koliko_clenov_harmonicne_vrste_potrebujemo_da_presezemo(meja):
    n = 1
    vsota = 0
    while vsota < meja:
        vsota += 1 / n
        # print(n, vsota)
        n += 1
    return n - 1