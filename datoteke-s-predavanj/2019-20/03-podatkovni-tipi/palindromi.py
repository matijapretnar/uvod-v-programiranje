def najdaljsi_podpalindrom(niz):
    if len(niz) <= 1:
        return niz
    elif niz[0] == niz[-1]:
        return niz[0] + najdaljsi_podpalindrom(niz[1:-1]) + niz[0]
    else:
        brez_prve = najdaljsi_podpalindrom(niz[1:])
        brez_zadnje = najdaljsi_podpalindrom(niz[:-1])
        return max(brez_prve, brez_zadnje, key=len)
