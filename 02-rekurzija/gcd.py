
# 42 = 99 * 0 + 42
# 99 = 42 * 2 + 15
# 42 = 15 * 2 + 12
# 15 = 12 * 1 + 3
# 12 = 3 * 4 + 0

def gcd(m, n):
    print(m, n)
    if m % n == 0:
        print("končal sem")
        return n
    elif m > n:
        print("naredim korak")
        return gcd(n, m % n)
    else:
        print("zamenjal ju bom")
        return gcd(n, m)

def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m % n)

def gcd(m, n):
    return m if n == 0 else gcd(n, m % n)
