def harmonicna_vrsta(m):
    vsota = 0
    n = 1
    while vsota < m:
        vsota = vsota + 1 / n
        n = n + 1
    return n - 1
