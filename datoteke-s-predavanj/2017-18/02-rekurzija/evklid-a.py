# 720 = 2 * g + 208
# 256 = 1 * 208 + 48
# 208 = 4 * 48 + 16
# 48 = 3 * 16 + 0
# 16 =


def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m % n)
