Iterabilni objekti *
==================

``zip`` in ``enumerate``
------------------------

Dostikrat želimo hkrati dostopati do elementov seznama in njihovih indeksov.

Predstavimo polinome s seznamom koeficientov, urejenim od prostega proti
vodilnemu členu. Polinom :math:`3 - x^2` bi tako predstavili s seznamom
``[3, 0, -1]``. Pri izračunu vrednosti polinoma želimo hkrati dostopati tako do
koeficientov kot do njihovih indeksov, ki ustrezajo potenci. To lahko storimo
na več načinov. Lahko se vozimo po indeksih in prek njih dostopamo do
koeficientov:

.. testcode::

    def vrednost_polinoma(koeficienti, tocka):
        '''Vrne vrednost polinoma z danimi koeficienti v dani točki.'''
        vsota = 0
        for i in range(len(koeficienti)):
            koeficient = koeficienti[i]
            vsota += koeficient * tocka ** i
        return vsota


.. doctest::

    >>> vrednost_polinoma([3, 0, 1], 1)
    4
    >>> vrednost_polinoma([3, 0, 1], 2)
    7

Lahko se vozimo po koeficientih in hkrati povečujemo števec indeksa:

.. testcode::

    def vrednost_polinoma(koeficienti, tocka):
        '''Vrne vrednost polinoma z danimi koeficienti v dani točki.'''
        vsota = 0
        i = 0
        for koeficient in koeficienti:
            vsota += koeficient * tocka ** i
            i += 1
        return vsota

Najbolj enostavno pa je, da uporabimo funkcijo ``enumerate``, ki vrne zaporedje
parov, v katerih so druge komponente vrednosti danega seznama, prve komponente
pa njihovi indeksi:

 .. doctest::
 
     >>> list(enumerate([20, 200, 2000]))
     [(0, 20), (1, 200), (2, 2000)]
     >>> list(enumerate('beseda'))
     [(0, 'b'), (1, 'e'), (2, 's'), (3, 'e'), (4, 'd'), (5, 'a')]

S pomočjo funkcije ``enumerate`` lahko vrednost polinoma izračunamo kot:

.. testcode::

    def vrednost_polinoma(koeficienti, tocka):
        '''Vrne vrednost polinoma z danimi koeficienti v dani točki.'''
        vsota = 0
        for i, koeficient in enumerate(koeficienti):
            vsota += koeficient * tocka ** i
        return vsota

Kot vidimo, lahko tudi v zanki ``for`` uporabimo razstavljanje naborov, in
pare, ki nam jih podaja ``enumerate``, takoj shranimo v dve spremenljivki.

.. caution::

    Paziti moramo, da indeksa ne računamo s pomočjo metode ``.index``, saj
    je ta način prvič neučinkovit, drugič pa ne bi vedno delovala pravilno, saj
    ``.index`` vrne indeks prve pojavitve iskane vrednosti:


    .. testcode::

        def napacna_vrednost_polinoma(koeficienti, tocka):
            '''Vrne vrednost polinoma z danimi koeficienti v dani točki.'''
            vsota = 0
            for koeficient in koeficienti:
                i = koeficienti.index(koeficient)
                vsota += koeficient * tocka ** i
            return vsota

    .. doctest::

        >>> vrednost_polinoma([0, 2, 0, 2], 3)
        60
        >>> napacna_vrednost_polinoma([0, 2, 0, 2], 3)
        12

    Ker je v spodnjem klicu funkcije metoda ``.index`` za indeks prve pojavitve
    vrednosti 2 obakrat vrnila 1, je funkcija vrnila :math:`2 \cdot 3^1 + 2 \cdot 3^1 = 6`
    namesto :math:`2 \cdot 3^1 + 2 \cdot 3^3 = 60`.


Podobno kot ``enumerate`` deluje funkcija ``zip``, ki sprejme več seznamov,
vrne pa zaporedje naborov istoležnih elementov:

.. doctest::

    >>> list(zip([10, 20, 30], [4, 5, 6]))
    [(10, 4), (20, 5), (30, 6)]
    >>> list(zip([10, 20, 30], [4, 5, 6], 'abc'))
    [(10, 4, 'a'), (20, 5, 'b'), (30, 6, 'c')]

Funkciji se reče ``zip``, ker združuje elemente različnih seznamov tako, kot
zadrga. Vrnjeno zaporedje ima toliko elementov, kot najkrajši argument funkcije:

    >>> list(zip([10, 20, 30], [4, 5, 6], 'ab'))
    [(10, 4, 'a'), (20, 5, 'b')]

S pomočjo funkcije ``zip`` lahko enostavno izračunamo skalarni produkt:

.. testcode::

    def skalarni_produkt(vektor1, vektor2):
        '''Vrne skalarni produkt dveh vektorjev iste dimenzije.'''
        assert len(vektor1) == len(vektor2)
        vsota = 0
        for x1, x2 in zip(vektor1, vektor2):
            vsota += x1 * x2
        return vsota


.. doctest::

    >>> skalarni_produkt([1, -2, 5], [-2, 5, 2])
    -2
