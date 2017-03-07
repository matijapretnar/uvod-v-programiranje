def vrednost_polinoma(koeficienti, tocka):
    '''Vrne vrednost polinoma z danimi koeficienti v dani točki.'''

    # Ta je napačna
    # vsota = 0
    # for koeficient in koeficienti:
    #     vsota += koeficient * tocka ** koeficienti.index(koeficient)
    # return vsota

    # vsota = 0
    # for n in range(len(koeficienti)):
    #     vsota += koeficienti[n] * tocka ** n
    # return vsota

    # vsota = 0
    # n = 0
    # for koeficient in koeficienti:
    #     vsota += koeficient * tocka ** n
    #     n += 1
    # return vsota

    vsota = 0
    for stopnja, koeficient in enumerate(koeficienti):
        vsota += koeficient * tocka ** stopnja
    return vsota
