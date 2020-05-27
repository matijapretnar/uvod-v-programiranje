def fakulteta(n):
    if n <= 1:
        return 1
    else:
        n_minus_1 = n - 1
        fakulteta_od_n_minus_1 = fakulteta(n_minus_1)
        n_krat_fakulteta_od_n_minus_1 = n * fakulteta_od_n_minus_1
        return n_krat_fakulteta_od_n_minus_1

def zmnozek(m, n):
    """Vrne produkt m (m + 1) ... (n - 1) n."""
    if m == n:
        return m
    else:
        k = (m + n) // 2
        return zmnozek(m, k) * zmnozek(k + 1, n)
