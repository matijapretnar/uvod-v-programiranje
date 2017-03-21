Seznami
=======

Če želimo delati z zaporedjem podatkov, uporabimo sezname.

Pisanje seznamov
----------------

Sename pišemo v oglatih oklepajih, med katerimi napišemo vrednosti, ločene z
vejicami, na primer ``[10, 20, 30]`` je seznam, ki vsebuje tri števila, ``[]``
pa prazen seznam. Če želimo, lahko vejico pišemo tudi za zadnjim elementom.
Seznami so lahko tudi gnezdeni. Na primer, matriko bi predstavili s seznamom
seznamov:

.. testcode::

    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

V sezname lahko spravimo vrednosti različnih tipov, na primer:

.. testcode::

    [1, True, [2, 5], "Niz", 3.14]

Vendar običajno sezname uporabimo za predstavitev homogene zbirke podatkov,
torej da so vse vrednosti istega tipa.



Operacije na seznamih
---------------------

Tako kot nize lahko tudi sezname stikamo z operacijo ``+`` in množimo s celimi števili:

.. doctest::

    >>> [10, 20, 30] + [6, 5, 4]
    [10, 20, 30, 6, 5, 4]
    >>> 4 * [1, 2]
    [1, 2, 1, 2, 1, 2, 1, 2]

Dolžino seznama dobimo s funkcijo ``len``:

.. doctest::

    >>> len([100, 200, 300])
    3
    >>> len([])
    0

Tudi na seznamih imamo na voljo predikata ``in`` in ``not in``, s katerima
ugotovimo, ali se nek element pojavlja v seznamu:

.. doctest::

    >>> 'Ema' in ['Ana', 'Bojan', 'Cvetka', 'David']
    False
    >>> 'Ana' in ['Ana', 'Bojan', 'Cvetka', 'David']
    True


.. testcode::

    def stevilo_dni(mesec, leto):
        if mesec == 2:
            return 29 if je_prestopno(leto) else 28
        elif mesec in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif mesec in [4, 6, 9, 11]:
            return 30


Indeksiranje in rezine
----------------------

Indeksiranje in rezine na seznamih delujejo tako kot na nizih:

.. doctest::

    >>> sez = [5, 3, 8, 2, 5, 2, 1, 2]
    >>> sez[0]
    5
    >>> sez[2]
    8
    >>> sez[len(sez) - 1]
    2
    >>> sez[-1]
    2
    >>> sez[:2]
    [5, 3]
    >>> sez[1:3]
    [3, 8]
    >>> sez[3:]
    [2, 5, 2, 1, 2]
    >>> sez[1:5:2]
    [3, 2]
    >>> sez[::2]
    [5, 8, 5, 1]

Če imamo gnezdene sezname, do elementov dostopamo z gnezdenimi indeksi:

    >>> mat = [[1, 0, 0], [0, -1, 2], [3, 1, 5]]
    >>> mat[0][0]
    1
    >>> mat[1][-1]
    2
