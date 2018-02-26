
Iskanje ničel z bisekcijo
-------------------------

Poglejmo si še enostaven algoritem, s katerim lahko približno izračunamo ničlo
zvezne realne funkcije :math:`f` na intervalu :math:`[a, b]`, če vemo, da sta
vrednosti :math:`f(a)` in :math:`f(b)` različno predznačeni.
Naj bo :math:`c = (a + b) / 2` sredina intervala.
Tedaj ločimo tri primere :math:`f(c)`:

* Če imamo srečo, je :math:`f(c) = 0`, zato smo našli ničlo in postopek lahko končamo.
  Sicer je :math:`f(c)` neničelno število, zatorej ima nek predznak.
* Če je predznak :math:`f(c)` različen od predznaka :math:`f(a)` lahko na podoben
  način nadaljujemo z iskanjem ničle na intervalu :math:`[a, c]`.
* V nasprotnem primeru pa mora biti predznak :math:`f(c)` različen od predznaka
  :math:`f(b)` (ker imata :math:`f(a)` in :math:`f(b)` različen predznak), zato
  lahko z iskanjem nadaljujemo na intervalu :math:`[c, b]`.

Ker interval vedno razdelimo na pol, postopku pravimo *bisekcija*. Ker lahko
realna števila poljubno delimo, se zgornji postopek ne bo nikoli ustavil (razen,
če imamo srečo in naletimo točno na ničlo). Toda ker nas zanima le približek
ničle, lahko postopek ustavimo takrat, ko se krajišči intervala razlikujeta za
dovolj majhno vrednost :math:`\varepsilon`. Načeloma v algoritmu prvo možnost
(ko je :math:`f(c) = 0`) kar izpustimo, saj je preveč redka, pa tudi brez nje
algoritem najde pravo rešitev.

V Pythonu bi algoritem zapisali kot:

.. testcode::

    def bisekcija(f, a, b, eps):
        '''Z metodo bisekcije izračuna ničlo f na intervalu [a, b].'''
        c = (a + b) / 2
        if b - a < eps:
            return c
        elif f(a) * f(c) < 0:
            return bisekcija(f, a, c, eps)
        else:
            return bisekcija(f, c, b, eps)


.. doctest::

    >>> import math
    >>> bisekcija(math.sin, 2, 4, 0.01)
    3.14453125
    >>> bisekcija(math.sin, 2, 4, 0.00001)
    3.141590118408203
    >>> bisekcija(math.sin, 2, 4, 10 ** -10)
    3.1415926536137704
    >>> bisekcija(math.sin, 2, 4, 1e-10)
    3.1415926536137704


Funkcije višjega reda
---------------------

Zgoraj lahko opazimo, da nam Python dopušča, da za argumente funkcij ne podajamo
le števil, temveč tudi druge funkcije. Pravimo, da podpira *funkcije višjega
reda*. Če želimo, lahko za argumente podamo tudi funkcije, ki smo jih definirali
sami:

.. testcode::

    def moj_f(x):
        return x ** 2 - 2

.. doctest::

    >>> bisekcija(moj_f, 1, 2, 0.000001)
    1.4142136573791504

Če se nam neke funkcije, ki bi jo uporabili samo v enem primeru (kot je ta zgoraj),
ne da poimenovati, lahko uporabimo *anonimne* oziroma *lambda* funkcije, v katerih
za telo napišemo enostaven izraz. Zgornji primer bi z njimi pisali kot:

.. doctest::

    >>> bisekcija(lambda x: x ** 2 - 2, 1, 2, 0.000001)
    1.4142136573791504

Funkcij z zapletenejšim telesom in tistih, v katerih uporabljemo več stavkov,
ne pišemo z lambdami. Tako ali tako je bolje, da zapletenejšim funkcijam damo
ime, da se vidi, kaj počnejo.
