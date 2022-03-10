def stevilo_clenov_da_harmonicna_vrsta_preseze(n):
    vsota, i = 0, 0
    while vsota < n:
        i = i + 1              # ali kar i += 1
        if i % 100000 == 0:
            print(i)
        vsota = vsota + 1 / i  # ali kar vsota += 1 / i
    return i
