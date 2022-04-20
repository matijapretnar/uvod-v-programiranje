def najvecji(*iterable):
    print(iterable)
    if len(iterable) == 1:
        iterable = iterable[0]
    najvecji = None
    for x in iterable:
        if najvecji == None or x > najvecji:
            najvecji = x
    return najvecji
