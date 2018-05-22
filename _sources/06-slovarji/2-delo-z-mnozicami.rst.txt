Delo z množicami *
================

.. testcode::

    def je_prastevilo(n):
        if n <= 2:
            return n == 2
        d = 3
        while d * d <= n:
            if n % d == 0:
                return False
            d += 2
        return True

.. code::

    majhna_prastevila = {2, 3, 5, 7, ..., 997}

    def je_prastevilo(n):
        if n <= majhna_prastevila[-1]:
            return n in majhna_prastevila
        d = 3
        while d * d <= n:
            if n % d == 0:
                return False
            d += 2
        return True

.. code::

    >>> s = {6, 2, 3}
    >>> len(s)
    3
    >>> max(s)
    6
    >>> sum(s)
    11
    >>> sez = [1, 5, 2, 4, 8, 1, 5, 3, 2, 1]
    >>> sum(sez)
    32
    >>> mn = set(sez)
    >>> sum(mn)
    23


.. code::

    >>> a = {1, 2, 3, 4}
    >>> a.add(5)
    >>> a
    {1, 2, 3, 4, 5}
    >>> a.remove(3)
    >>> a
    {1, 2, 4, 5}


.. code::

    >>> {1, 2, 3, 4} | {3, 4, 5, 6}
    {1, 2, 3, 4, 5, 6}
    >>> {1, 2, 3, 4} & {3, 4, 5, 6}
    {3, 4}
    >>> {1, 2, 3, 4} - {3, 4, 5, 6}
    {1, 2}
    >>> 1 in {1, 2, 3, 4}
    True
    >>> 2 in {3, 4, 5, 6}
    False
    >>> list({1, 2, 3})


.. testcode::

    def direktna_slika(f, a):
        slika = set()
        for x in a:
            slika.add(f(x))
        return slika

    def direktna_slika(f, a):
        return {f(x) for x in a}

.. code::

    >>> direktna_slika(lambda x: x ** 2, {-5, -3, 1, 2})
    {1, 4, 9, 25}
    >>> {x ** 2 for x in range(1, 30) if x % 5 == 3}
    {64, 324, 9, 169, 784, 529}
    >>> {x for x in range(1, 100) if x % 5 == 3 and x % 3 != 0}
    {98, 68, 38, 8, 73, 43, 13, 83, 53, 23, 88, 58, 28}


.. testcode::

    {
        'Borut': {'Janez', 'Miro', 'Karl'},
        'Janez': {'Borut', 'Karl'},
        'Miro': {'Borut', 'Karl'},
        'Karl': {'Borut', 'Janez', 'Miro'},
        'Igor': set(),
    }

    def priporoci_prijatelje(omrezje, oseba):
        novi_prijatelji = set()
        for prijatelj in omrezje[oseba]:
            for prijatelj_prijatelja in omrezje[prijatelj]:
                novi_prijatelji.add(prijatelj_prijatelja)
        return novi_prijatelji - {oseba} - omrezje[oseba]
