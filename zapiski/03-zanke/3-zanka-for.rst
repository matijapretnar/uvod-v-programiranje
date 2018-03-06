Zanka ``for``
=============

Zanko ``while`` torej uporabimo takrat, kadar želimo ukaze ponavljati, dokler
velja nek pogoj. Včasih pa že vnaprej vemo, kolikokrat bomo te ukaze ponovili.
Na primer, funkcijo za izračun fakultete bi lahko pisali kot:

.. testcode::

    def fakulteta(n):
        '''Vrne fakulteto naravnega števila n.'''
        produkt = 1
        i = 1
        while i <= n:
            produkt *= i
            i += 1
        return produkt

vendar vemo, da se bo zanka izvedla natanko enkrat za vsako število od n do 0.
Poleg tega se nam hitro zgodi, da vrstico ``i += 1`` po nesreči pozabimo ali
napišemo kot ``i + 1`` ali kot ``i = 1``, zaradi česar se zanka izvaja v
neskončnost. Za primere, ko vemo, kolikokrat izvedemo določeno kodo, raje
uporabimo zanko ``for``.

.. code::

    for spremenljivka in podane_vrednosti:
        # stavki, ki se izvedejo
        # po enkrat za vsako izmed
        # podanih vrednost spremenljivke

Na primer, fakulteto števila 10 bi lahko izračunali kot:

.. testcode::

    fakulteta10 = 1
    for i in range(1, 11):
        fakulteta10 *= i

.. doctest::

    >>> fakulteta10
    3628800

V zanki ``for`` smo uporabili funkcijo ``range``, ki vrne vsa cela števila v razponu od vključno prvega do tistega pred drugim (tako kot pri rezinah). V naši zanki ``for`` se spremenljivka ``i`` torej sprehodi po vseh
vrednostih od ``1`` do ``10``. Koda se obnaša tako, kot če bi pisali:

.. testcode::

    fakulteta10 = 1
    i = 1
    fakulteta10 *= i
    i = 2
    fakulteta10 *= i
    i = 3
    fakulteta10 *= i
    i = 4
    fakulteta10 *= i
    i = 5
    fakulteta10 *= i
    i = 6
    fakulteta10 *= i
    i = 7
    fakulteta10 *= i
    i = 8
    fakulteta10 *= i
    i = 9
    fakulteta10 *= i
    i = 10
    fakulteta10 *= i

Funkcijo ``fakulteta`` pa bi napisali kot:


.. testcode::

    def fakulteta(n):
        '''Vrne fakulteto naravnega števila n.'''
        produkt = 1
        for i in range(1, n + 1):
            produkt *= i
        return produkt


Zanka ``for`` na nizih
----------------------

Po vseh znakih danega niza se lahko sprehodimo z zanko ``for``:

.. testcode::

    def je_samoglasnik(crka):
        return crka in 'aeiouAEIOU'

    def stevilo_samoglasnikov(niz):
        '''Vrne število samoglasnikov v danem nizu.'''
        stevilo = 0
        for znak in niz:
            if je_samoglasnik(znak):
                stevilo += 1
        return stevilo

    def brez_samoglasnikov(niz):
        '''Vrne niz enak danemu, le da smo iz njega izpustili vse samoglasnike.'''
        niz_brez_samoglasnikov = ''
        for znak in niz:
            if not je_samoglasnik(znak):
                niz_brez_samoglasnikov += znak
        return niz_brez_samoglasnikov

.. doctest::

    >>> stevilo_samoglasnikov('Uvod v programiranje')
    7
    >>> brez_samoglasnikov('Uvod v programiranje')
    'vd v prgrmrnj'


Manjkajoča veja ``else``
------------------------

Če želimo, lahko vejo ``else`` tudi izpustimo (tako v običajnem kot v
razširjenem pogojnem stavku). V tem primeru se ob neizpolnjevanju pogoja ne
zgodi nič. Na ta način bi izračun osnovnih točk lahko pisali tudi kot:

.. doctest::

    osnovne_tocke = 60
    if k_tocka >= 170:
        osnovne_tocke = 120

Torej, ``osnovne_tocke`` najprej nastavimo na 60, v primeru da gre za letalnico,
pa jih popravimo na 120. Vrstni red izvajanja je seveda pomemben. Če bi pisali

.. doctest::

    if k_tocka >= 170:
        osnovne_tocke = 120
    osnovne_tocke = 60

bi osnovne točke vedno nastavili na 60.


Stavki ``break``, ``continue`` in ``pass`` (vsebina še manjka)
--------------------------------------------------------------

