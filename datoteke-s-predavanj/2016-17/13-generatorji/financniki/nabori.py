def vsi_pari(iter1, iter2):
    '''Generator vseh parov elementov, ki jih podajata iteratorja
       iter1 in iter2.'''
    for x1 in iter1:
        for x2 in iter2:
            yield (x1, x2)


def funkcija_z_vec_argumenti(x, y, *preostali, **preostali_imenovani):
    return preostali_imenovani


def vsi_nabori(*iterabilni):
    if len(iterabilni) == 0:
        yield ()
    else:
        for glava in iterabilni[0]:
            for rep in vsi_nabori(*iterabilni[1:]):
                yield (glava,) + rep


# list(vsi_nabori([10, 20], [3, 4]))
# vsi_nabori([3, 4])
# vsi_nabori(([3, 4],))
#
#
# def f(*argumenti):
#     ...
#
# f(1, 2, 3)
#   argumenti = (1, 2, 3)
#   argumenti[1] = (2, 3)
#   f(argumenti[1:])
#     argumenti_ob_drugem_klicu = (2, 3)


# [1, 10, 20], [5, 4], 'abcd'

# 1
# (1, 5, 'a')
# (1, 5, 'b')
# (1, 5, 'c')
# (1, 5, 'd')
# (1, 4, 'a')
# (1, 4, 'b')
# (1, 4, 'c')
# (1, 4, 'd')

# 10
# (10, 5, 'a')
# (10, 5, 'b')
# (10, 5, 'c')
# (10, 5, 'd')
# (10, 4, 'a')
# (10, 4, 'b')
# (10, 4, 'c')
# (10, 4, 'd')

# 20
# ...