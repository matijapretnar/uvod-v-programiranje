Bisekcija
=========

Izračun korena
--------------

Poglejmo si enostaven algoritem, s katerim lahko izračunamo kvadratni koren pozitivnega števila. Recimo, da že vemo, da se koren števila :math:`n` nahaja na intervalu :math:`[a, b]` (npr. vemo, da se zagotovo nahaja na intervalu :math:`[0, n]`). Naj bo :math:`c = (a + b) / 2` sredina intervala. Tedaj ločimo tri primere:

* Če imamo srečo, je :math:`c^2 = n`, zato smo našli koren in postopek lahko končamo.
* Če je :math:`c^2 > n`, je tudi :math:`c > \sqrt{n}`, zato lahko na podoben način nadaljujemo z iskanjem korena na intervalu :math:`[a, c]`.
* V nasprotnem primeru pa mora biti :math:`c^2 < n` in :math:`c < \sqrt{n}`, zato lahko z iskanjem nadaljujemo na intervalu :math:`[c, b]`.

Ker interval vedno razdelimo na pol, postopku pravimo *bisekcija*. Ker lahko realna števila poljubno delimo, se zgornji postopek ne bo nikoli ustavil (razen, če imamo srečo in naletimo točno na koren). Toda ker nas zanima le približek korena, lahko postopek ustavimo takrat, ko se krajišči intervala razlikujeta za dovolj majhno vrednost :math:`\varepsilon`. Načeloma v algoritmu prvo možnost (ko je :math:`c^2 = n`) kar izpustimo, saj je preveč redka, pa tudi brez nje algoritem najde pravo rešitev.

V Pythonu bi algoritem zapisali kot:

.. testcode::

    def kvadratni_koren(n, eps):
        '''Z metodo bisekcije poišče koren števila n.'''
        a, b = 0, n
        while b - a > eps:
            c = (a + b) / 2
            if c * c > n:
                b = c
            else:
                a = c
        return c


.. doctest::

    >>> kvadratni_koren(10, 1e-5)
    3.1622791290283203
    >>> kvadratni_koren(10, 1e-10)
    3.1622776602307567
    >>> kvadratni_koren(10, 1e-15)
    3.162277660168379

Neobvezni argumenti
-------------------

Včasih imamo za nekatere argumente funkcij v mislih že prav določeno vrednost. Na primer, za izračun logaritma potrebujemo dve števili: osnovo in argument (tudi logaritmand). Toda velikokrat za osnovo vzamemo :math:`10`, zato namesto :math:`\log_{10} x` pišemo kar :math:`\log x`. Tudi pri Pythonu je podobno. Če se nam ob klicu funkcije ne ljubi navajati vrednosti vseh argumentov, lahko za nekatere od njih v prvi vrstici definicije navedemo privzeto vrednost. Na primer, pri funkciji ``kvadratni_koren`` ne pričakujemo, da bo uporabnik vedno znova vnašal natančnost, na katero želi izračunati koren. Če želimo, da ima ``eps`` privzeto vrednost ``1e-15``, lahko napišemo:

.. testcode::

    def kvadratni_koren(n, eps=1e-15):
        '''Z metodo bisekcije poišče koren števila n.'''
        a, b = 0, n
        while b - a > eps:
            c = (a + b) / 2
            if c * c > n:
                b = c
            else:
                a = c
        return c

Tedaj se bo vedno uporabila privzeta vrednost za tiste argumente, ki jih ne podamo izrecno.

    >>> kvadratni_koren(10, eps=1e-5)
    3.1622791290283203
    >>> kvadratni_koren(10, eps=1e-15)
    3.162277660168379
    >>> kvadratni_koren(10)
    3.162277660168379

Klic deluje tudi, če neobveznih argumentov ne poimenujemo, vendar lahko to vodi do zmede, če je argumentov več, zato se takih klicev izogibamo.

.. doctest::

    >>> kvadratni_koren(10, 1e-15)
    3.162277660168379


Iskanje ničel
-------------

Na podoben način lahko približno izračunamo ničlo zvezne realne funkcije :math:`f` na intervalu :math:`[a, b]`, če vemo, da sta vrednosti :math:`f(a)` in :math:`f(b)` različno predznačeni. Če je :math:`c = (a + b) / 2` zopet sredina intervala, ločimo tri primere:

* Če imamo srečo, je :math:`f(c) = 0`, zato smo našli ničlo in postopek lahko končamo. Sicer je :math:`f(c)` neničelno število, zatorej ima nek predznak.
* Če je predznak :math:`f(c)` različen od predznaka :math:`f(a)` lahko na podoben način nadaljujemo z iskanjem ničle na intervalu :math:`[a, c]`.
* V nasprotnem primeru pa mora biti predznak :math:`f(c)` različen od predznaka :math:`f(b)` (ker imata :math:`f(a)` in :math:`f(b)` različen predznak), zato lahko z iskanjem nadaljujemo na intervalu :math:`[c, b]`.

Podobno kot prej bi algoritem zapisali kot:

.. testcode::

    def bisekcija(f, a, b, eps):
        '''Z metodo bisekcije izračuna ničlo f na intervalu [a, b].'''
        while b - a > eps:
            c = (a + b) / 2
            if f(a) * f(c) < 0:
                b = c
            else:
                a = c
        return c



.. doctest::

    >>> import math
    >>> bisekcija(math.sin, 2, 4, 0.01)
    3.1484375
    >>> bisekcija(math.sin, 2, 4, 0.00001)
    3.1415939331054688
    >>> bisekcija(math.sin, 2, 4, 10 ** -10)
    3.141592653642874
    >>> bisekcija(math.sin, 2, 4, 1e-10)
    3.141592653642874


Funkcije višjega reda
---------------------

Zgoraj lahko opazimo, da nam Python dopušča, da za argumente funkcij ne podajamo le števil, temveč tudi druge funkcije. Pravimo, da podpira *funkcije višjega reda*. Če želimo, lahko za argumente podamo tudi funkcije, ki smo jih definirali sami:

.. testcode::

    def moj_f(x):
        return x ** 2 - 2

.. doctest::

    >>> bisekcija(moj_f, 1, 2, 0.000001)
    1.4142141342163086

Če se nam neke funkcije, ki bi jo uporabili samo v enem primeru (kot je ta zgoraj), ne da poimenovati, lahko uporabimo *anonimne* oziroma *lambda* funkcije, v katerih za telo napišemo enostaven izraz. Zgornji primer bi z njimi pisali kot:

.. doctest::

    >>> bisekcija(lambda x: x ** 2 - 2, 1, 2, 0.000001)
    1.4142141342163086

Funkcij z zapletenejšim telesom in tistih, v katerih uporabljemo več stavkov, ne pišemo z lambdami. Tako ali tako je bolje, da zapletenejšim funkcijam damo ime, da se vidi, kaj počnejo.
