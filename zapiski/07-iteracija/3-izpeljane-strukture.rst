Izpeljane strukture *
===================

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
