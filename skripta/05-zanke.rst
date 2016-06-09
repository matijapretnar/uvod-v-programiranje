Zanke
=====

Z rekurzijo dosežemo, da nek del kode izvedemo večkrat. 

Zanka ``while``
---------------

Z zanko ``while`` določene ukaze izvajamo toliko časa, dokler velja dani pogoj.

.. code::

    while pogoj:
        stavki
        ki_naj_se_izvajajo
        dokler_velja_pogoj

Izračunajmo stopnjo največje potence števila 2, ki še deli število 1580160. To
storimo tako, da število zaporedoma celoštevilsko delimo z 2 in ob vsakem
deljenju števec stopnje povečamo za 1. Ukaze ponavljamo toliko časa, dokler je
ostanek pri deljenju z 2 enak 0:

.. testcode::

    n = 1580160
    stopnja = 0
    while n % 2 == 0:
        n //= 2
        stopnja += 1

Ko se izvajanje zaključi, lahko preverimo, da velja

.. doctest::

    >>> stopnja
    7

Zgornji program lahko pretvorimo v splošnejšo funkcijo:

.. testcode::

    def stopnja_najvecje_potence(n, k):
        '''Vrne stopnjo največje potence števila k, ki še deli n.'''
        stopnja = 0
        while n % k == 0:
            n //= k
            stopnja += 1
        return stopnja

.. doctest::

    >>> stopnja_najvecje_potence(1580160, 2)
    7
    >>> stopnja_najvecje_potence(81, 3)
    4

Isto funkcijo bi lahko napisali tudi z rekurzijo:

.. testcode::

    def stopnja_najvecje_potence_rek(n, k):
        '''Vrne stopnjo največje potence števila k, ki še deli n.'''
        if n % k == 0:
            return 1 + stopnja_najvecje_potence_rek(n // k, k)
        else:
            return 0

.. doctest::

    >>> stopnja_najvecje_potence_rek(1580160, 2)
    7
    >>> stopnja_najvecje_potence_rek(81, 3)
    4

V praksi pa za tiste programe, pri katerih neko stvar ponavljamo toliko časa,
dokler velja določen pogoj, raje uporabimo zanko ``while``, saj je učinkovitejša
(vsaj v Pythonu, v drugih jezikih je rekurzija ravno tako učinkovita). Od funkcij,
ki smo jih že videli, bi z zanko ``while`` lahko napisali Evklidov algoritem in
bisekcijo:

.. testcode::

    def gcd(m, n):
        '''Vrne največji skupni delitelj števil m in n.'''
        while n != 0:
            m, n = n, m % n
        return m

    def bisekcija(f, a, b, eps=1e-12):
        '''Z metodo bisekcije izračuna ničlo f na intervalu [a, b].'''
        assert f(a) * f(b) < 0
        while b - a > eps:
            c = (a + b) / 2
            if f(a) * f(c) < 0:
                b = c
            else:
                a = c
        return c

Kot smo videli, se Python pritoži, če gremo pri rekurziji pregloboko. Običajno
se to zgodi takrat, kadar smo rekurzijo napisali tako, da se ne ustavi. Vendar
računalnik tega ne more vedeti, zato se Python ustavi takrat, ko naredimo
približno 1000 rekurzivnih klicev:

.. doctest::

    >>> stopnja_najvecje_potence_rek(2 ** 985, 2)
    985
    >>> stopnja_najvecje_potence_rek(2 ** 986, 2)
    Traceback (most recent call last):
      ...
      File "...", line 4, in stopnja_najvecje_potence_rek
      File "...", line 4, in stopnja_najvecje_potence_rek
      File "...", line 4, in stopnja_najvecje_potence_rek
      File "...", line 4, in stopnja_najvecje_potence_rek
      File "...", line 4, in stopnja_najvecje_potence_rek
      File "...", line 3, in stopnja_najvecje_potence_rek
    RecursionError: maximum recursion depth exceeded in comparison

Pri zankah teh težav ni:

.. doctest::

    >>> stopnja_najvecje_potence(2 ** 985, 2)
    985
    >>> stopnja_najvecje_potence(2 ** 986, 2)
    986
    >>> stopnja_najvecje_potence(2 ** 10000, 2)
    10000

Seveda tudi pri zanki ``while`` obstaja nevarnost, da se njeno izvajanje nikoli
ne zaključi. Na primer, če bi poklicali

.. code::

    >>> stopnja_najvecje_potence(12345, 1)

bi bil ostanek pri deljenju z 1 v pogoju vedno enak 0, zato bi zanka tekla v
neskončnost. Ko se naveličamo čakanja, lahko pritisnemo ``Ctrl-C`` in izvajanje
prekinemo.

Zanka ``for``
-------------

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

    for spremenljivka in mozne_vrednosti:
        stavki_ki_se_izvedejo
        po_enkrat_za_vsako
        mozno_vrednost_spremenljivke

Na primer, fakulteto števila 10 bi lahko izračunali kot:

.. testcode::

    fakulteta10 = 1
    for i in range(1, 11):
        fakulteta10 *= i

.. doctest::

    >>> fakulteta10
    3628800

V zanki ``for`` smo uporabili funkcijo ``range``, ki vrne vsa cela števila v
razponu od vključno prvega do tistega pred drugim (zakaj zadnjega ne šteje, bomo
še videli). . V naši zanki ``for`` se spremenljivka ``i`` torej sprehodi po vseh
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


Stavki ``break``, ``continue`` in ``pass`` (vsebina še manjka)
--------------------------------------------------------------
