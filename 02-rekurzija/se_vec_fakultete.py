def fakulteta(n):
    """Vrne n! = n (n - 1) ... 2 1"""
    # Ker je n! = n (n - 1) ... 2 1 = n (n - 1)!
    # lahko funkcijo prevedemo na samo sebe
    # (taki funkciji pravimo rekurzivna)
    if n == 0:
        return 1
    else:
        n_minus_1 = n - 1
        fakulteta_od_n_minus_1 = fakulteta(n_minus_1)
        produkt = n * fakulteta_od_n_minus_1
        return produkt

fakulteta(10)

fakulteta900 = fakulteta(900)

def vecja_fakulteta(n):
    if n < 900:
        return fakulteta(n)
    elif n == 900:
        return fakulteta900
    else:
        return n * vecja_fakulteta(n - 1)

def produkt_zaporednih(m, n):
    """Vrne produkt števil m * (m + 1) * ... * (n - 2) * (n - 1)"""
    if m == n:
        return 1
    else:
        k = (m + n) // 2
        return produkt_zaporednih(m, k) * k * produkt_zaporednih(k + 1, n)

def fmf(n):
    return produkt_zaporednih(1, n + 1)
