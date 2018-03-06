Zanka ``for``
=============

Zanko ``while`` torej uporabimo takrat, kadar želimo ukaze ponavljati, dokler velja nek pogoj. Včasih pa že vnaprej vemo, kolikokrat bomo te ukaze ponovili. Na primer, funkcijo za izračun fakultete bi lahko pisali kot:

.. testcode::

    def fakulteta(n):
        '''Vrne fakulteto naravnega števila n.'''
        produkt = 1
        i = 1
        while i <= n:
            produkt *= i
            i += 1
        return produkt

vendar vemo, da se bo zanka izvedla natanko enkrat za vsako število od n do 0. Poleg tega se nam hitro zgodi, da vrstico ``i += 1`` po nesreči pozabimo ali napišemo kot ``i + 1`` ali kot ``i = 1``, zaradi česar se zanka izvaja v neskončnost. Za primere, ko vemo, kolikokrat izvedemo določeno kodo, raje uporabimo zanko ``for``.

.. code::

    for spremenljivka in podane_vrednosti:
        # stavki, ki se izvedejo
        # po enkrat za vsako izmed
        # podanih vrednost spremenljivke


Zanka ``for`` na razponih
-------------------------

Na primer, fakulteto števila 10 bi lahko izračunali kot:

.. testcode::

    fakulteta10 = 1
    for i in range(1, 11):
        fakulteta10 *= i

.. doctest::

    >>> fakulteta10
    3628800

V zanki ``for`` smo uporabili funkcijo ``range``, ki vrne vsa cela števila v razponu od vključno prvega do tistega pred drugim (tako kot pri rezinah). V naši zanki ``for`` se spremenljivka ``i`` torej sprehodi po vseh vrednostih od ``1`` do ``10``. Koda se obnaša tako, kot če bi pisali:

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

Kot vidimo zgoraj, lahko vejo ``else`` tudi izpustimo (tako v običajnem kot v
razširjenem pogojnem stavku). V tem primeru se ob neizpolnjevanju pogoja ne
zgodi nič.


Stavki ``break``, ``continue`` in ``pass``
------------------------------------------

V zankah lahko uporabimo tudi posebne ukaze, ki spreminjajo običajen potek programa. Stavek ``break`` prekine trenutno zanko. Na primer:

.. testcode::

    for n in range(1, 5):
        print(n)
        if n == 2 or n == 3:
            break
        print('x')

izmenično izpisuje števila od 1 do 4 ter znak ``x``. V trenutku, ko pride do števila 2, ki zadošča pogoju ``n == 2 or n == 3``, izvajanje zanke v celoti prekine, zato izpiše le

.. testoutput::

    1
    x
    2

Primer je napisan za zanko ``for``, vendar enako deluje tudi za zanko ``while``.

Stavek ``continue`` zanke ne ustavi, temveč le preskoči preostanek trenutnega obhoda zanke in gre nazaj na začetek z naslednjo vrednostjo. Na primer:


.. testcode::

    for n in range(1, 5):
        print(n)
        if n == 2 or n == 3:
            continue
        print('x')

pri številih 2 in 3, ki zadoščata pogoju, preskoči izpis znaka ``x``, ki bi moral slediti. Celoten izpis je tako:

.. testoutput::

    1
    x
    2
    3
    4
    x

Tudi stavek ``continue`` deluje tako za zanko ``for`` kot za zanko ``while``.

Stavek ``pass`` pa ne stori ničesar. Na primer:

.. testcode::

    for n in range(1, 5):
        print(n)
        if n == 2 or n == 3:
            pass
        print('x')

pri številih 2 in 3, ki zadoščata pogoju, vstopi v pogojni stavek, vendar tam ne stori ničesar. Tako je izpis enak, kakor bi bil za program brez pogojnega stavka:

.. testoutput::

    1
    x
    2
    x
    3
    x
    4
    x

Stavek ``pass`` lahko uporabljamo kjerkoli v Pythonu, ne le v zankah. Najpogosteje ga uporabimo takrat, kadar Python zahteva, da napišemo vsaj en ukaz, vendar ne želimo storiti ničesar. Recimo, da imamo program:

.. code::

    for x in range(100):
        if x % 2 == 0:
            print(x, 'je sod')
        else:
            print(x, 'je lih')

in za trenutek želimo izklopiti izpisovanje sodih števil. Če bi napisali le

.. code::

    for x in range(100):
        if x % 2 == 0:
            # print(x, 'je sod')
        else:
            print(x, 'je lih')

bi se Python pritožil, da je prva veja pogojnega stavka prazna, saj komentarje ignorira. Seveda bi lahko celoten program preuredili v

.. code::

    for x in range(100):
        if x % 2 != 0:
            print(x, 'je lih')

vendar tega ne želimo (sploh pri večjih programih). S pomočjo stavka ``pass`` pa lahko napišemo

.. code::

    for x in range(100):
        if x % 2 == 0:
            # print(x, 'je sod')
            pass
        else:
            print(x, 'je lih')

Tudi če se odločimo, da bi zopet vklopili izpisovanje, lahko stavek ``pass`` pustimo v kodi, ker ne stori ničesar.
