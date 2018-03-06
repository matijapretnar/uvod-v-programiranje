Zanka ``while``
===============

Z zanko ``while`` določene ukaze izvajamo toliko časa, dokler velja dani pogoj.

.. code::

    while pogoj:
        # stavki, 
        # ki naj se izvajajo
        # dokler velja pogoj

Na primer, program

.. testcode::

    n = 12
    while n < 1000:
        n = n * 2
        print(n)

bo ``n`` nastavil na 12, nato pa ga toliko časa podvojeval, dokler njegova vrednost ne bo dosegla 1000. Program bo tako izpisal:

.. testoutput::

    24
    48
    96
    192
    384
    768
    1536

V programih bomo pogostokrat novo vrednost spremenljivke izračunali tako, da bomo spremenili staro (zato tudi govorimo o _spremenljivkah_). Na primer, ko bomo šteli vsa praštevila med 1 in 1000000, bomo imeli spremenljivko, ki bo imela na začetku vrednost 0, nato pa jo bomo ob vsakem praštevilu povečali za 1. V ta namen lahko namesto ``n = n * 2`` pišemo kar operator ``n *= 2``, saj je ``*=`` operacija, ki spremenljivko na levi pomnoži z vrednostjo na desni. Tudi za ostale operacije obstajajo podobne bližnjice, na primer ``-=``, ``*=``, ``//=`` in tako naprej.

.. doctest::

    >>> x = 3
    >>> x += 2
    >>> x *= 4
    >>> x
    20

Za primer izračunajmo stopnjo največje potence števila 2, ki še deli število 1580160. To storimo tako, da število zaporedoma celoštevilsko delimo z 2 in ob vsakem deljenju števec stopnje povečamo za 1. Ukaze ponavljamo toliko časa, dokler je ostanek pri deljenju z 2 enak 0:

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

    >>> stopnja_najvecje_potence(81, 3)
    4
    >>> stopnja_najvecje_potence(1580160, 2)
    7

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

V praksi pa za tiste programe, pri katerih neko stvar ponavljamo toliko časa, dokler velja določen pogoj, raje uporabimo zanko ``while``, saj je učinkovitejša (vsaj v Pythonu, v drugih jezikih je rekurzija ravno tako učinkovita). Tako bi z zanko ``while`` lahko napisali tudi Evklidov algoritem:

.. testcode::

    def gcd(m, n):
        '''Vrne največji skupni delitelj števil m in n.'''
        while n != 0:
            m, n = n, m % n
        return m

Kot smo videli, se Python pritoži, če gremo pri rekurziji pregloboko. Običajno se to zgodi takrat, kadar smo rekurzijo napisali tako, da se ne ustavi. Vendar računalnik tega ne more vedeti, zato se Python ustavi takrat, ko naredimo približno 1000 rekurzivnih klicev:

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

