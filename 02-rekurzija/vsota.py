def vsota_stevil(n):
    """Vrne vsoto števil 1 + 2 + ... + n"""
    if n == 0:
        return 0
    else:
        # vsota od 1 do n 
        # = 1 + 2 + ... + (n - 1) + n
        # = (1 + 2 + ... + (n - 1)) + n
        # = (vsota od 1 do n - 1) + n
        return vsota_stevil(n - 1) + n

def vsota_stevil_kot_bi_jo_naredil_gauss(n):
    """Vrne vsoto števil 1 + 2 + ... + n"""
    return (n * (n + 1)) // 2

def vsota_stevil_med(m, n):
    """Vrne vsoto števil m + (m + 1) + ... + n"""
    if m > n:
        return 0
    else:
        # m + (m + 1) + ... + n
        # = m + ((m + 1) + ... + n)
        return m + vsota_stevil_med(m + 1, n)
