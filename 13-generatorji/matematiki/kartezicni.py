# iterator (iterator)
# - objekt, ki nam ob vsakem klicu next da neko vrednost

# iterabilni objekt (iterable)
# - objekt, ki ima iterator po svojih vrednostih (npr. nizi, seznami)

# generator (generator)
# - iterabilni objekt, ki ga dobimo na enostaven način z uporabo
#   stavka yield


def generiraj_pare(iter1, iter2):
    '''Generator, ki zaporedoma vrača vse pare, kjer je prva
       komponenta v iter1, druga pa v iter2.'''
    for x1 in iter1:
        for x2 in iter2:
            yield (x1, x2)

def generiraj_nabore(*iterabilni_objekti):
    '''Generator, ki zaporedoma vrača vse nabore iz danih
       iterabilnih objektov..'''
    if len(iterabilni_objekti) == 0:
        yield ()
    else:
        for glava in iterabilni_objekti[0]:
            for rep in generiraj_nabore(*iterabilni_objekti[1:]):
                yield (glava,) + rep

def funkcija(predsednica, *clani):
    return clani
    print("{} je predsednica od: {}".format(predsednica, ", ".join(clani)))

def f(x, y):
    return x + y


# generiraj_pare([1, 2, 3], [4, 5])
# (1, 4)
# (1, 5)
# (2, 4)
# (2, 5)
# (3, 4)
# (3, 5)


# generiraj_nabore([1, 2, 3], [4, 5], 'ab')
# (1, 4, 'a')
# (1, 4, 'b')
# (1, 5, 'a')
# (1, 5, 'b')
# ...
# (3, 5, 'b')
