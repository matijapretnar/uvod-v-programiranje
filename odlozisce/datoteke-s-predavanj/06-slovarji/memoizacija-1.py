def mem_kvadrat(x):
    kvadrati = {}
    if x not in kvadrati:
        print('Računam', x)
        y = x ** 2
        kvadrati[x] = y
    else:
        print('Oh, za', x, 'pa točno vem rezultat, ker sem ga sam izračunal!')
    return kvadrati[x]

stolpi = {}
def stevilo_stolpov(n):
    if n not in stolpi:
        print('Računam', n)
        if n < 0:
            y = 0
        elif n == 0:
            y = 1
        else:
            na_vrhu_1 = stevilo_stolpov(n - 1)
            na_vrhu_2 = stevilo_stolpov(n - 2)
            na_vrhu_3 = stevilo_stolpov(n - 3)
            y = na_vrhu_1 + na_vrhu_2 + na_vrhu_3
        stolpi[n] = y
    return stolpi[n]

# Brez memoizacije bi bili klici:
#
# # stevilo_stolpov(10)
    # stevilo_stolpov(9)
        # stevilo_stolpov(8)
            # ...
        # stevilo_stolpov(7)
            # ...
        # stevilo_stolpov(6)
            # ...
    # stevilo_stolpov(8)
        # stevilo_stolpov(7)
            # ...
        # stevilo_stolpov(6)
            # ...
        # stevilo_stolpov(5)
            # ...
    # stevilo_stolpov(7)
        # ...
