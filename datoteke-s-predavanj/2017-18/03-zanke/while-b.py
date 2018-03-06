vsota = 0
n = 1
while vsota < 15:
    n += 1
    vsota += 1 / n

def gcd(m, n):
    while n > 0:
        print(m, n)
        m, n = n, m % n
    return m
