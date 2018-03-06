vsota = 0
n = 1
while vsota <= 15:
    # print(vsota, 'bom prištel', 1 / n)
    vsota += 1 / n
    n += 1


def gcd(m, n):
    while n != 0:
        o = m % n
        m = n
        n = o
    return m


def fibonacci(n):
    a = 0
    b = 1
    m = 0
    while m < n:
        a, b = b, a + b
        m += 1
    return a
