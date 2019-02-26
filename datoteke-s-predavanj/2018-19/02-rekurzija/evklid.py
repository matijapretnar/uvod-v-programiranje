# EVKLIDOV ALGORITEM
#
# IDEJA:
# Če je
#   m = k * n + o,
# potem velja
#   gcd(m, n) = gcd(n, o)
#
# DOKAZ:
# Ker je
#   m = k * n + o,
# bo vsak skupni delitelj števil n in o delil desno stran,
# zato bo delil tudi levo stran, torej m, zato je tudi skupni
# delitelj števil m in n. Iz tega sledi
#  gcd(m, n) >= gcd(n, o)
# Podobno je
#   o = m - k * n,
# zato vsak skupni delitelj števil m in n deli tudi n in o, torej
#  gcd(n, o) >= gcd(m, n)
# zato je 
#  gcd(m, n) = gcd(n, o)
#
# PRIMER:
#   gcd(256, 720)    256 = 0 * 720 + 256
# = gcd(720, 256)    720 = 2 * 256 + 208
# = gcd(256, 208)    256 = 1 * 208 + 48
# = gcd(208, 48)     208 = 4 * 48  + 16
# = gcd(48, 16)      48  = 3 * 16  + 0
# = gcd(16, 0)
# = 16


def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m % n)

gcd(256, 720)