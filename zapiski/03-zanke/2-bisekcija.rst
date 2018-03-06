Bisekcija
=========

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


Neobvezni argumenti
-------------------

Včasih imamo za nekatere argumente funkcij v mislih že prav določeno vrednost.
Na primer, za izračun logaritma potrebujemo dve števili: osnovo in argument
(tudi logaritmand). Toda velikokrat za osnovo vzamemo :math:`10`, zato namesto
:math:`\log_{10} x` pišemo kar :math:`\log x`. Tudi pri Pythonu je podobno. Če
se nam ob klicu funkcije ne ljubi navajati vrednosti vseh argumentov, lahko za
nekatere od njih v prvi vrstici definicije navedemo privzeto vrednost. Na primer, pri funkciji
``splosni_fibonacci`` želimo, da imata ``a`` in ``b`` privzeti vrednosti 0 in 1:

.. testcode::

    def splosni_fibonacci(n, a=0, b=1):
        '''Vrne n-ti člen Fibonaccijevega zaporedja, ki se začne z a in b.'''
        if n == 0:
            return a
        elif n == 1:
            return b
        else:
            return splosni_fibonacci(n - 1, b, a + b)

Tedaj se bo vedno uporabila privzeta vrednost za tiste argumente, ki jih ne
podamo izrecno.

    >>> splosni_fibonacci(35)
    9227465
    >>> splosni_fibonacci(500)
    139423224561697880139724382870407283950070256587697307264108962948325571622863290691557658876222521294125
    >>> splosni_fibonacci(25, b=2)
    150050
    >>> splosni_fibonacci(25, a=1, b=-1)
    -28657

Klic deluje tudi, če neobveznih argumentov ne poimenujemo, vendar lahko to vodi
do zmede, zato se takih klicev izogibamo.

.. doctest::

    >>> splosni_fibonacci(25, 1, -1)
    -28657




