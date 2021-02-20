def abs(x):
    if x >= 0:
        return x
    else:
        return -x


def predznak(x):
    if x < 0:
        return -1
    else:
        if x > 0:
            return 1
        else:
            return 0


def predznak(x):
    if x == 0:
        return 0
    elif x > 0:
        return 1
    elif x < 0:
        return -1


def fakulteta(n):
    if n == 0:
        return 1
    else:
        return fakulteta(n - 1) * n
