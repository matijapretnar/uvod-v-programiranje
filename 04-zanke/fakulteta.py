def fakulteta_z_while(m):
    produkt = 1
    n = 1
    while n <= m:
        produkt = produkt * n
        n = n + 1
    return produkt

def fakulteta_s_for(m):
    produkt = 1
    for n in range(1, m + 1):
        produkt = produkt * n
    return produkt
