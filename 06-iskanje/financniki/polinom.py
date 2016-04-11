def vrednost(koeficienti, x):
    '''Izračuna vrednost polinoma z danimi koeficienti v točki x.'''
    vsota = 0
    for stopnja, koef in enumerate(koeficienti):
        vsota += koef * x ** stopnja
    return vsota
