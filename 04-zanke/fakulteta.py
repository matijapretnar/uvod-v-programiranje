def fakulteta_while(n):
    produkt = 1
    i = 1
    while i <= n:
        produkt *= i
        i += 1
    return produkt

def fakulteta_for(n):
    produkt = 1
    for i in range(1, n + 1):
        produkt *= i
    return produkt