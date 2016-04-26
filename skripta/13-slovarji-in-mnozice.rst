Slovarji in množice
===================


Primeri uporabe slovarjev
-------------------------

.. testcode::

    nujne_telefonske_stevilke = {
      'center za obveščanje': 112,
      'policija': 113,
      'informacije': 1188,
      'točen čas': 195
    }

.. code::   

    slo_ang = {
      'abak': 'abacus',
      'abalienacija': 'abalienation',
      'abderit': 'abderite',
      ...
      'žvrkljati': 'whisk'
    }


.. testcode::

    rimske_stevilke = {
        1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
        6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX',
        10: 'X', 20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L',
        100: 'C', 500: 'D', 1000: 'M'
    }

.. testcode::

    vrli_parlamentarci = {
        'DeSUS': 10, 'NSi': 5, 'SD': 6, 'SDS': 21,
        'SMC': 36, 'ZaAB': 4, 'ZL': 6
    }

    met_kocke = {
        1: 1/6, 2: 1/6, 3: 1/6, 4: 1/6, 5: 1/6, 6: 1/6
    }

    met_dveh_kock = {
        2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, 7: 6/36,
        8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
    }


.. testcode::

    matrika = [
        [0, 0, 1, 0, 0, 0],
        [5, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]

    redka_matrika = {
        (0, 2): 1,
        (1, 0): 5,
        (1, 1): 2,
        (2, 4): 3,
        (4, 2): 1
    }


.. testcode::

    avtocestni_kriz = {
        'LJ': {'KR': 26, 'CE': 73, 'PO': 51, 'NM': 72},
        'PO': {'LJ': 51, 'KP': 64, 'GO': 63},
        'CE': {'MB': 54, 'LJ': 73},
        'MB': {'CE': 54, 'MS': 60},
        'GO': {'PO': 63},
        'KR': {'LJ': 26},
        'MS': {'MB': 60},
        'NM': {'LJ': 72},
        'KP': {'GO': 64}
    }


.. testcode::

    knjiga = {
        'naslov': 'Prišel je velikanski lev',
        'avtor': 'Kristina Brenkova',
        'ilustrator': 'Polona Lovšin',
        'strani': 31,
        'leto': 2010,
        'ključne besede': ['lev', 'Afrika', 'Matic', 'otroci']
    }

    nakljucni_slovar = {
        1: 'abc',
        (2, '3'): 'D',
        '456': 789
    }

Operacije na slovarjih
----------------------

.. doctest::

    >>> s = {'a': 6, 'b': 2, 'c': 3}
    >>> len(s)
    3
    >>> max(s)
    'c'
    >>> max(s.values())
    6
    >>> sum(s.values())
    11

.. doctest::

    >>> s = {'a': 6, 'b': 2, 'c': 3}
    >>> s
    {'a': 6, 'b': 2, 'c': 3}
    >>> s['a']
    6
    >>> s['b']
    2
    >>> s['d']
    Traceback (most recent call last):
      File "<pyshell#20>", line 1, in <module>
        s['d']
    KeyError: 'd'
    >>> s.get('a')
    6
    >>> s.get('d')
    >>> s.get('d', 0)
    0
    >>> 'b' in s
    True
    >>> 'd' in s
    False

.. testcode::

    def prestej_pojavitve(niz):
        pojavitve = {}
        for znak in niz:
            if znak in pojavitve:
                pojavitve[znak] += 1
            else:
                pojavitve[znak] = 1
        return pojavitve

    def prestej_pojavitve(niz):
        pojavitve = {}
        for znak in niz:
            pojavitve[znak] = pojavitve.get(znak, 0) + 1
        return pojavitve


.. doctest::

    >>> prestej_pojavitve('abrakadabra')



Spreminjanje slovarjev
----------------------

.. doctest::

    >>> s = {'a': 6, 'b': 2, 'c': 3}
    >>> s['b'] = 8
    >>> s
    {'b': 8, 'a': 6, 'c': 3}
    >>> s['d'] = 10
    >>> s
    {'b': 8, 'a': 6, 'c': 3, 'd': 10}
    >>> del s['b']
    >>> s
    {'d': 10, 'a': 6, 'c': 3}


Zanka ``for`` na slovarjih
--------------------------

.. doctest::

    >>> s = {'a': 6, 'b': 2, 'c': 3}
    >>> list(s.keys())
    ['b', 'a', 'c']
    >>> list(s.values())
    [2, 6, 3]
    >>> list(s.items())
    [('b', 2), ('a', 6), ('c', 3)]

.. testcode::

    def najvecja_vrednost(s):
        # Ideja je podobna kot pri seznamih: po vrsti gledamo vse pare ključev in
        # vrednosti v slovarju - vsakič, ko vidimo še večjo vrednost, si zapomnimo
        # njen ključ.

        # Ker slovarji niso urejeni po vrsti, ne moremo začeti s prvim elementom.
        # Lahko pa si pomagamo z metodo popitem(), ki iz slovarja odstrani naključen
        # ključ in njegovo vrednost.
        max_k, max_v = s.popitem()
        for k, v in s.items():
            if v > max_v:
                max_k, max_v = k, v
        return max_k, max_v


.. code::

    >>> {n: stevilo_deliteljev(n) for n in range(20, 29)}
    {20: 6, 21: 4, 22: 4, 23: 2, 24: 8, 25: 3, 26: 4, 27: 4, 28: 6}


Množice
-------


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

.. doctest::

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


.. doctest::

    >>> a = {1, 2, 3, 4}
    >>> a.add(5)
    >>> a
    {1, 2, 3, 4, 5}
    >>> a.remove(3)
    >>> a
    {1, 2, 4, 5}


.. doctest::

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

.. doctest::

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
