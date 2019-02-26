def fakulteta(n):
    if n <= 1:
        return 1
    else:
        n_minus_ena = n - 1
        fakulteta_od_n_minus_ena = fakulteta(n_minus_ena)
        zmnozek = n * fakulteta_od_n_minus_ena
        return zmnozek
