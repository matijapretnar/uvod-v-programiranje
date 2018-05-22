Izpeljani seznami
-----------------

Python omogoča, da sezname tvorimo na enostaven način z **izpeljanimi seznami**, ki so oblike ``[izraz for spremenljivka in mozne_vrednosti]``, podobno kot v matematiki množice pišemo kot :math:`\{ 2 \cdot n \mid n \in \{1, \dots, 9\}\}`:
.. doctest::

    >>> [2 * n for n in range(1, 10)]
    [2, 4, 6, 8, 10, 12, 14, 16, 18]
    >>> potence = [2 ** n for n in range(10)]
    >>> potence
    [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    >>> [n - 1 for n in potence]
    [0, 1, 3, 7, 15, 31, 63, 127, 255, 511]
    >>> [int(stevka) for stevka in str(3141592)]
    [3, 1, 4, 1, 5, 9, 2]
    
Če želimo, lahko v izpeljani seznamih oblike ``[izraz for spremenljivka in mozne_vrednosti if pogoj]`` s pogojem določimo, katere elemente želimo:

.. doctest::

    >>> [2 * n for n in range(1, 10) if n % 3 == 1]
    [2, 8, 14]



Metode na seznamih
------------------


Seveda bi obe funkciji lepše napisali s pomočjo izpeljanih seznamov:

.. testcode::

    def pozitivni_elementi(seznam):
        '''Vrne seznam vseh pozitivnih elementov danega seznama.'''
        return [element for element in seznam if element > 0]

    def vsota_pozitivnih_elementov(seznam):
        '''Vrne seznam vseh pozitivnih elementov danega seznama.'''
        return sum([element for element in seznam if element > 0])
        # ali pa kar
        # return sum(pozitivni_elementi(seznam))




S pomočjo vzorca za preostale argumente bi tako funkcijo napisali tako, da bi
najprej preverili, koliko argumentov smo dobili, nato pa ustrezno poiskali
maksimum:

.. testcode::

    def maksimum(*argumenti):
        '''
        Ob več argumentih vrne največjega.
        Ob enem argumentu vrne njegov največji element.
        '''
        if len(argumenti) == 0:       # Če nismo dobili nobenega argumenta,
            return None               # vrnemo None.
        if len(argumenti) == 1:       # Če smo dobili en argument,
            kandidati = argumenti[0]  # iščemo maksimum med njegovimi elementi.
        else:                         # Če smo dobili več argumentov,
            kandidati = argumenti     # iščemo maksimum med njimi.

        # Uporabimo znan postopek za iskanje največjega elementa.
        najvecji = None
        for kandidat in kandidati:
            if najvecji is None or najvecji < kandidat:
                najvecji = kandidat
        return najvecji


.. doctest::

    >>> maksimum([3, 5], [4, 1])
    [4, 1]
    >>> maksimum([3, 5, 4, 1])
    5
    >>> maksimum(3, 5, 4, 1)
    5
