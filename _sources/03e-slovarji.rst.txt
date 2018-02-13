Slovarji
========


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
