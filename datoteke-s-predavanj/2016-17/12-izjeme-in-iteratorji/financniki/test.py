def fakulteta(n):
    raise NotImplementedError


def binomski_simbol(n, k):
    return fakulteta(n) // (fakulteta(k) * fakulteta(n - k))


for x in range(1, 10):
    print('Začenjam korak {}'.format(x))
    if x == 5:
        continue
    print('Sem na koraku {}'.format(x))
    print('Končujem korak {}'.format(x))