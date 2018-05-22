Delo s slovarji *
===============

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

Operacije na slovarjih
----------------------

.. code::

    >>> s = {'a': 6, 'b': 2, 'c': 3}
    >>> len(s)
    3
    >>> max(s)
    'c'
    >>> max(s.values())
    6
    >>> sum(s.values())
    11

.. code::

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


.. code::

    >>> prestej_pojavitve('abrakadabra')



Spreminjanje slovarjev
----------------------

.. code::

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

.. code::

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
