Seznami in nabori
=================

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

Spreminanje in brisanje elementov
---------------------------------

Za razliko od nizov lahko vrednosti v seznamih tudi spreminjamo:

.. doctest::

    >>> sez = [5, 3, 8, 2, 5, 7, 1, 2]
    >>> sez[3] = 200
    >>> sez
    [5, 3, 8, 200, 5, 7, 1, 2]
    >>> del sez[5]
    >>> sez
    [5, 3, 8, 200, 5, 1, 2]
    >>> sez[-1] = 500
    >>> sez
    [5, 3, 8, 200, 5, 1, 500]
    >>> sez[1:3] = [100, 300]
    >>> sez
    [5, 100, 300, 200, 5, 1, 500]
    >>> sez[2:5] = []
    >>> sez
    [5, 100, 1, 500]
    >>> sez[2:2] = [0, 0, 0]
    >>> sez
    [5, 100, 0, 0, 0, 1, 500]
    >>> sez[2] = [20, 20, 20]
    >>> sez
    [5, 100, [20, 20, 20], 0, 0, 1, 500]
    >>> del sez[1:4]
    >>> sez
    [5, 0, 1, 500]


Zanka ``for`` na nizih
----------------------

Po vseh elementih danega seznama se lahko sprehodimo z zanko ``for``:

.. testcode::

    def vsota_elementov(sez):
        '''Vrne vsoto elementov v danem seznamu.'''
        vsota = 0
        for x in sez:
            vsota += x
        return vsota

    def najvecji_element(sez):
        '''Vrne največji element v danem seznamu. Če ga ni, vrne None'''
        if len(sez) == 0:
            return
        najvecji = sez[0]
        for x in sez:
            najvecji = max(x, najvecji)
        return najvecji

.. doctest::

    >>> vsota_elementov([10, 2, 4000, 300])
    4312
    >>> najvecji_element([10, 2, 4000, 300])
    4000

Seveda lahko uporabimo tudi vgrajene funkcije:

.. doctest::

    >>> sum([10, 2, 4000, 300])
    4312
    >>> min([10, 2, 4000, 300])
    2
    >>> max([10, 2, 4000, 300])
    4000


Metode na seznamih
------------------

* ``sez.append(x)``
    Dodaj element `x` na konec seznama ``sez``.

* ``sez.extend(sez2)``
    Na konec seznama ``sez`` dodaj vse elemente iz seznama ``sez2``.


* ``sez.insert(i, x)``
    Pred element na mestu ``i`` v seznamu ``sez`` vstavi element ``x``.

* ``sez.remove(x)``
    Iz seznama ``sez`` odstrani prvo pojavitev vrednosti ``x``.


* ``sez.pop(i=-1)``
    Vrni element na mestu ``i`` v seznamu ``sez`` in odstrani ta element iz seznama.
    Če indeksa ``i`` ne podamo, metoda odstrani zadnji element.

* ``sez.clear()``
    Iz seznama ``sez`` pobriši vse elemente.

* ``sez.index(x)``
    Vrni prvo mesto, na katerem se v seznamu ``sez`` nahaja vrednost ``x``.

* ``sez.count(x)``
    Vrni število pojavitev vrednosti ``x`` v seznamu ``sez``.

* ``sez.sort(key=None, reverse=False)``
    Na mestu uredi seznam glede na vrednosti funkcije ``key``. Če parameter
    ``reverse`` nastavimo na ``True``, bo seznam urejen padajoče.

* ``sez.reverse()``
    Obrni seznam ``sez`` na glavo.

.. doctest::

    >>> sez = [66.25, 333, 333, 1, 1234.5]
    >>> (sez.count(333), sez.count(66.25), sez.count('x'))
    (2, 1, 0)
    >>> sez.insert(2, -1)
    >>> sez.append(333)
    >>> sez
    [66.25, 333, -1, 333, 1, 1234.5, 333]
    >>> sez.index(333)
    1
    >>> sez.remove(333)
    >>> sez
    [66.25, -1, 333, 1, 1234.5, 333]
    >>> sez.reverse()
    >>> sez
    [333, 1234.5, 1, 333, -1, 66.25]
    >>> sez.sort()
    >>> sez
    [-1, 1, 66.25, 333, 333, 1234.5]
    >>> sez.pop()
    1234.5
    >>> sez
    [-1, 1, 66.25, 333, 333]

Nabori
------

Nabori se obnašajo podobno kot seznami, le da njihovih vrednosti ne moremo
spreminjati. Pišemo jih tako kot sezname, le med običajne oklepaje: ``(1, 2, 3)``.
Nabor z enim elementom pišemo kot ``(1, )`` (razmislite, zakaj ga ne pišemo kot
``(1)``). V seznamih so elementi običajno vsi istega tipa in pomenijo iste stvari,
v naborih pa so lahko tudi različnih tipov, pomen vsakega pa je odvisen od mesta:

.. testcode::

    student = ('Ana', 'Novak', 27162315)
    ucenci = ['Ana', 'Bojan', 'Cvetka', 'David']
    datum = (30, 'marec', 2016)
    datumi = [(30, 'marec', 2016), (1, 'april', 2016), (25, 'junij', 2016)]
