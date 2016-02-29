Rekurzija
=========

Če za trenutek odmislimo, da od računalnikov pričakujemo tudi to, da kaj
preberejo s tipkovnice, kaj izrišejo na zaslon, ali pa se kaj pogovarjajo z
drugimi računalniki, lahko s tisto malega, kar smo spoznali v prejšnjem
poglavju, napišemo čisto vse, kar je računalnik sposoben izračunati. Tista
stvar, ki nam vse to omogoča je rekurzija.

Rekurzivni klici
----------------

Videli smo, da lahko iz funkcij kličemo tudi druge funkcije. Na primer, v
funkciji ``povrsina_tetraedra`` smo poklicali funkcijo ``ploscina_trikotnika``,
v tej pa vgrajeno funkcijo ``math.sqrt``. V resnici pa lahko v funkciji
pokličemo tudi funkcijo samo. Takemu klicu pravimo **rekurzivni klic**.
Poglejmo, kako bi izračunali :math:`n! = n \cdot (n - 1) \dots 3 \cdot 2 \cdot
1`. Kot vidimo velja :math:`n! = n \cdot (n - 1)!`, zato bomo :math:`n!`
izračunali tako, da bomo :math:`n` pomnožili z :math:`(n - 1)!`. Toda od kod
bomo dobili tega? Preprosto, :math:`n - 1` bomo pomnožili z :math:`(n - 2)!`. Od
kod pa tega? Ja iz :math:`(n - 3)!`. In tako naprej vse do :math:`2!`, ki ga
bomo dobili iz :math:`1!`, tega pa iz :math:`0!`, ki je po definiciji enak
:math:`1`.

Torej lahko funkcijo, ki računa fakulteto, napišemo tako, da najprej pogleda
svoj argument ``n``. Če je enak 1, vrne 1, sicer pa izračunamo tako, da ``n``
pomnožimo z rezultatom klica ``fakulteta(n - 1)``:

.. testcode::

    def fakulteta(n):
        '''Vrne fakulteto naravnega števila n.'''
        if n == 0:
            return 1
        else:
            return n * fakulteta(n - 1)

ali s pogojnim izrazom kot:

.. testcode::

    def fakulteta(n):
        '''Vrne fakulteto naravnega števila n.'''
        return 1 if n == 0 else n * fakulteta(n - 1)

.. doctest::

    >>> fakulteta(1)
    1
    >>> fakulteta(5)
    120
    >>> fakulteta(10)
    3628800

Še en primer rekurzivne definicije so Fibonaccijeva števila. Velja :math:`F_0 = 0`,
:math:`F_1 = 1`, za vse :math:`n \ge 2` pa velja in :math:`F_{n} = F_{n - 1} + F_{n - 2}`.
Funkcijo tedaj napišemo podobno na podoben način kot zgornjo: če
je ``n`` enak 0, vrnemo 0, sicer pogledamo, ali je enak 1. V tem primeru vrnemo
1. Če pa tudi 1 ni enak, mora biti večji ali enak 2, zato se pokličemo
rekurzivno.

.. testcode::

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

.. doctest::

    >>> fibonacci(3)
    2
    >>> fibonacci(4)
    3
    >>> fibonacci(5)
    5
    >>> fibonacci(20)
    6765

Tudi ta funkcija ima še svoje težave, zato se je še ne naučite, vendar se bomo s
tem ukvarjali malo kasneje.


Evklidov algoritem
------------------

Zdaj pa je že čas, da si pogledamo še naš prvi pravi algoritem. Algoritem je
zaporedje korakov, s katerimi dobimo iskani rezultat. Načeloma lahko pod besedo
algoritem razumemo tudi zaporedje korakov, s katerimi si skuhamo jajca (vzemi
posodo, odpri pipo, postavi posodo pod pipo, ko je posoda dovolj polna, …),
ampak ponavadi si jo prihranimo za postopke, s katerimi izračunamo želene
vrednosti.

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

V zadnjem klicu je ``1e-10`` krajši zapis za :math:`1 \cdot 10^{-10}`. V tem
zapisu plavajočih števil ločeno zapišemo decimalke (čemur rečemo *mantisa*),
nato pa še eksponent. Na primer ``3.2445e2`` je število :math:`324,45 = 3,2445 \cdot 10^2`)

Neobvezni argumenti
-------------------

Včasih imamo za nekatere argumente funkcij v mislih že prav določeno vrednost.
Na primer, za izračun logaritma potrebujemo dve števili: osnovo in argument
(tudi logaritmand). Toda velikokrat za osnovo vzamemo :math:`10`, zato namesto
:math:`\log_{10} x` pišemo kar :math:`\log x`. Tudi pri Pythonu je podobno. Če
se nam ob klicu funkcije ``bisekcija`` ne da vedno znova navajati vrednosti
argumenta ``eps``, lahko pišemo:

.. testcode::

    def bisekcija(f, a, b, eps=1e-10):
        '''Z metodo bisekcije izračuna ničlo f na intervalu [a, b].'''
        c = (a + b) / 2
        if b - a < eps:
            return c
        elif f(a) * f(c) < 0:
            return bisekcija(f, a, c, eps)
        else:
            return bisekcija(f, c, b, eps)

Tedaj bo Python vsakič, ko bomo funkciji podali le tri argumente, za vrednost
argumenta ``eps`` vzel ``1e-10``. Če pa želimo vrednost vseeno določiti, pa jo
lahko:

.. doctest::

    >>> import math
    >>> bisekcija(math.sin, 2, 4, eps=1e-10)
    3.1415926536137704
    >>> bisekcija(math.sin, 2, 4)
    3.1415926536137704
    >>> bisekcija(math.sin, 2, 4, eps=0.01)
    3.14453125

Klic deluje tudi, če neobveznih argumentov ne poimenujemo, vendar to vodi do
zmede.

.. doctest::

    >>> bisekcija(math.sin, 2, 4, 0.01)
    3.14453125


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
