Algoritmi
=========

Algoritem je zaporedje korakov, s katerimi dobimo iskani rezultat. Načeloma
lahko pod besedo algoritem razumemo tudi zaporedje korakov, s katerimi si
skuhamo jajca (vzemi posodo; odpri pipo; postavi posodo pod pipo; ko je posoda
dovolj polna, zapri pipo; …), ampak mi si jo bomo prihranili za postopke, s
katerimi izračunamo želene vrednosti.


Evklidov algoritem
------------------

Za prvi algoritem se spodobi, da si pogledamo najstarejši znani algoritem in
sicer Evklidov algoritem za iskanje navečjega skupnega delitelja dveh števil.
Naj bo :math:`d` največji skupni delitelj števil :math:`m` in :math:`n`. Pišimo
:math:`m = k \cdot n + o`, kjer je :math:`0 \le o < n`. Torej: :math:`o` je
ostanek pri deljenju števila :math:`m` z :math:`n`. Ker e :math:`d` deli :math:`n`,
deli tudi :math:`k \cdot n`. Poleg tega :math:`d` deli tudi :math:`m`, zato
deli tudi :math:`o = m - k \cdot n`. Velja tudi obratno, če :math:`d` deli
:math:`n` in :math:`o`, potem deli tudi :math:`m = k \cdot n + o`.

Zato lahko iskanje največjega skupnega delitelja števil :math:`m` in :math:`n`
prevedemo na iskanje največjega skupnega delitelja števil :math:`n` in
:math:`o`. Videti je, kot da se vrtimo v krogu, vendar se ne. Poglejmo, kaj
se zgodi:

1. Največji skupni delitelj števil :math:`456` in :math:`123` je enak
   največjemu skupnemu delitelju števil :math:`123` in :math:`456 - 3 \cdot 123 = 87`.
2. Največji skupni delitelj števil :math:`123` in :math:`87` je enak
   največjemu skupnemu delitelju števil :math:`87` in :math:`123 - 1 \cdot 87 = 36`.
3. Največji skupni delitelj števil :math:`87` in :math:`36` je enak
   največjemu skupnemu delitelju števil :math:`36` in :math:`123 - 2 \cdot 36 = 15`.
4. Največji skupni delitelj števil :math:`36` in :math:`15` je enak
   največjemu skupnemu delitelju števil :math:`15` in :math:`36 - 2 \cdot 15 = 6`.
5. Največji skupni delitelj števil :math:`15` in :math:`6` je enak
   največjemu skupnemu delitelju števil :math:`6` in :math:`15 - 2 \cdot 6 = 3`.
6. Največji skupni delitelj števil :math:`6` in :math:`3` je enak
   največjemu skupnemu delitelju števil :math:`3` in :math:`6 - 2 \cdot 3 = 0`.

Postopka ne moremo več nadaljevati, ker ne moremo deliti z nič. Kaj pa je
največji skupni delitelj števil 3 in 0? Ja, 3 vendar. Torej, ko je drugo število
enako 0, je prvo število ravno njun največji skupni delitelj, po vseh prejšnjih
sklepih pa tudi največji skupni delitelj vseh prejšnjih parov vključno s prvim.

Evklidov algoritem je torej sledeč: če je :math:`n = 0`, potem je največji skupni
delitelj števil :math:`m` in :math:`n` enak kar :math:`m`, sicer pa je enak
največjemu skupnemu delitelju števil :math:`n` in :math:`o`, kjer je :math:`o`
ostanek pri deljenju :math:`m` z :math:`n`.
Ta postopek enostavno prevedemo v Python:

.. testcode::

    def gcd(m, n):
        '''Vrne največji skupni delitelj števil m in n.'''
        if n == 0:
            return m
        else:
            return gcd(n, m % n)

ali s pogojnim izrazom kot

.. testcode::

    def gcd(m, n):
        '''Vrne največji skupni delitelj števil m in n.'''
        return m if n == 0 else gcd(n, m % n)

Pri tem je ``gcd`` (*greatest common divisor*) običajna oznaka za največjega
skupnega delitelja.

.. doctest::

    >>> gcd(456, 123)
    3

Algoritem deluje tudi, kadar je :math:`n < m`, saj je v tem primeru
:math:`n = 0 \cdot m + n`, zato v naslednjem koraku njuni mesti zamenjamo in
nadaljujemo kot prej.


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
