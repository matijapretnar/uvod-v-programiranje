# F_0 = 0
# F_1 = 1
# F_n = F_{n - 1} + F_{n - 2}

def fibonacci(n):
    """Vrne n-to Fibonaccijevo število F_n"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(6)

def izpisi_fibonaccije(n):
    """Izpiše števila F_0, F_1, ..., F_n"""
    if n >= 0:
        izpisi_fibonaccije(n - 1)
        print(n, fibonacci(n))

    #             F_5
    #        F_4                    F_3
    #  F_3         F_2            F_2     F_1
    # F_2 F_1    F_1 F_0       F_1 F_0

# 0 1 1 2 3 5 8 13 21 34 ...
#             ^
#             |
#             6 

# 1 1 2 3 5 8 13 21 34 ...


# 10 10 20 30 50 80 130 210 340 ...

# a b a+b a+2b 2a+3b 3a+5b ...  xa+yb
#                                 ^
#                                 |
#                                 n

# b a+b a+2b 2a+3b 3a+5b ...  xa+yb
#                               ^
#                               |
#                             n - 1

def posploseni_fibonacci(n, a=0, b=1):
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return posploseni_fibonacci(n - 1, a=b, b=(a + b))
