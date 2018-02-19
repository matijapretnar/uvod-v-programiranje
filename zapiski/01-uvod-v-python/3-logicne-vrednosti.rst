Logične vrednosti
=================

Poleg števil Python pozna tudi logični vrednosti ``True`` in ``False``, ki označujeta resnico in neresnico. Logične vrednosti ponavadi dobimo kot rezultat primerjav, kot so enakost ``==``, neenakost ``!=`` ali urejenostne relacije ``<``, ``>``, ``<=``, ``>=``, ter prek logičnih operacij ``and``, ``or`` in ``not``.

.. doctest::

    >>> 1 + 1 == 3
    False
    >>> 3 != 2
    True
    >>> True and False
    False
    >>> not (5 == 10)
    True
    >>> 3 < 5 or 10 > 20
    True


Pogojni stavek
--------------

Logične vrednosti uporabimo v *pogojnih stavkih* (oziroma *stavkih ``if``*) oblike

.. code::

    if pogoj:
        # stavki, ki jih izvedemo,
        # ko pogoj drži
    else:
        # stavki, ki jih izvedemo,
        # ko pogoj ne drži

Ključnima besedama ``if``/``else`` in pripadajočim stavkom pravimo tudi *veji pogojnega stavka*. Stavke v obeh vejah moramo zamakniti za štiri presledke tako kot v funkcijah.

Na primer, če izvedemo program

.. testcode::

    x = 5
    if x < 10:
        y = 2 * x
    else:
        y = 3 * x - 1
    x = y + 7

se bo izvedla veja ``if``, zato bo ``x`` na koncu enak 17, ``y`` pa 10. V primeru, da bi bila začetna vrednost ``x = 12``, pa bi se izvedla veja ``else`` in vrednost ``x`` bi na koncu bila 42, vrednost ``y`` pa 35.

Pogojne stavke lahko pišemo tudi v funkcijah. Na primer, funkcijo, ki računa absolutno vrednost, lahko s pomočjo pogojnega stavka napišemo kot:

.. testcode::

    def absolutna_vrednost(x):
        if x >= 0:
            return x
        else:
            return -x

.. doctest::

    >>> absolutna_vrednost(-5)
    5
    >>> absolutna_vrednost(3)
    3


Razširjeni pogojni stavek
-------------------------

Če bi želeli vrniti predznak števila, pa moramo ločiti tri primere: negativno število, nič in pozitivno število. To lahko storimo kot:


.. testcode::

    def predznak(x):
        if x < 0:
            return -1
        else:
            if x == 0:
                return 0
            else:
                return 1

Zgornji pogojni stavek je malo nerodno zapisan. Ker se nam bo dostikrat zgodilo, da se ne bomo odločali le med dvema primeroma, temveč med večimi, nam Python omogoča splošnejše pogojne stavke oblike:

.. code::

    if pogoj1:
        # stavki, ki jih izvedemo,
        # ko pogoj1 drži
    elif pogoj2:
        # stavki, ki jih izvedemo,
        # ko pogoj1 ne drži, ampak drži pogoj2
    elif pogoj3:
        # stavki, ki jih izvedemo,
        # ko tudi pogoj2 ne drži, ampak drži pogoj3
    else:
        # stavki, ki jih izvedemo,
        # ko noben od pogojev ne drži

Beseda ``elif`` je okrajšava za ``else``-``if``. Funkcijo za izračun predznaka bi lepše zapisali kot

.. testcode::

    def predznak(x):
        if x < 0:
            return -1
        elif x == 0:
            return 0
        else:
            return 1
