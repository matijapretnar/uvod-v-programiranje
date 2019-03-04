# F0 = 0
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        f_n_1 = fibonacci(n - 1)
        f_n_2 = fibonacci(n - 2)
        f_n = f_n_1 + f_n_2
        return f_n

# a, b, a + b, a + 2b, 2a + 3b, 3a + 5b, ..., F_n(a, b)
#                                              /\
#                                               |  
# b, a + b, a + 2b, 2a + 3b, 3a + 5b, ..., F_(n-1)(b, a + b)
#                                           /\
#                                            |  

def posploseni_fibonacci(n, a, b):
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return posploseni_fibonacci(n - 1, b, a + b)

def hitri_fibonacci(n):
    return posploseni_fibonacci(n, 0, 1)
