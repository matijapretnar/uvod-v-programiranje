Funkcije
========

Ploščino trikotnika s stranicami :math:`a, b, c` lahko izračunamo po Heronovi
formuli

.. math::

    \sqrt{s (s - a) (s - b) (s - c)}

kjer je :math:`s = (a + b + c) / 2`. Ploščino trikotnika s stranicami 4, 13 in 15
bi v Pythonu lahko torej izračunali s programom:

.. testcode::

    import math
    
    a, b, c = 4, 13, 15
    s = (a + b + c) / 2
    ploscina = math.sqrt(s * (s - a) * (s - b) * (s - c))

Tedaj je

.. doctest::

    >>> ploscina
    24.0

Kako pa bi izračunali površino tetraedra, ki ima za lica štiri trikotnike?
Načeloma bi lahko pisali:

.. testcode::

    a, b, c, d, e, f = 896, 1073, 1073, 990, 1073, 1073
    s_abc = (a + b + c) / 2
    ploscina_abc = math.sqrt(s_abc * (s_abc - a) * (s_abc - b) * (s_abc - c))
    s_aef = (a + e + f) / 2
    ploscina_aef = math.sqrt(s_aef * (s_aef - a) * (s_aef - e) * (s_aef - f))
    s_bdf = (b + d + f) / 2
    ploscina_bdf = math.sqrt(s_bdf * (s_bdf - b) * (s_bdf - d) * (s_bdf - f))
    s_cde = (c + d + e) / 2
    ploscina_cde = math.sqrt(s_cde * (s_cde - c) * (s_cde - d) * (s_cde - e))
    povrsina = ploscina_abc + ploscina_aef + ploscina_bdf + ploscina_cde

Kot vidimo, to ni najbolj pregledno. V taki kodi z veliko verjetnostjo naredimo
kakšno napako. Bolje je, da uporabimo funkcije. Že prej smo uporabili nekaj
vgrajenih funkcij, na primer ``min`` in ``max``. Python pa nam omogoča, da si
funkcije definiramo tudi sami.


Definicije lastnih funkcij
--------------------------

Definicija funkcije, ki izračuna ploščino trikotnika, je sledeča:

.. testcode::

    import math

    def ploscina_trikotnika(a, b, c):
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

Oglejmo si njene sestavne dele. Vsaka definicija funkcije se začne s ključno
besedo ``def``, ki ji sledi ime funkcije, v našem primeru
``ploscina_trikotnika``, tej pa v oklepajih našteti argumenti, ki jih funkcija
sprejme. Funkcije lahko sprejmejo različno število argumentov. Naša sprejme tri
argumente, ki jih bomo shranili v spremenljivke ``a``, ``b`` in ``c``. 

Nato sledi *telo funkcije*, torej ukazi, ki naj se izvedejo, ko funkcijo
pokličemo. Tako kot veje pogojnega stavka zamaknemo tudi celotno telo funkcije,
da se jasno vidi, kaj vse spada v definicijo funkcije. Prvo vrstico telesa smo
že videli, v drugi pa z ukazom ``return`` povemo, katero vrednost naj vrne
funkcija. Tako definirano funkcijo potem kličemo na enak način kot vgrajene
funkcije.

.. doctest::

    >>> ploscina_trikotnika(4, 13, 15)
    24.0

S pomočjo funkcije ``ploscina_trikotnika`` lahko tudi na veliko bolj pregleden
način zapišemo funkcijo za izračun površine tetraedra:

.. testcode::

    def povrsina_tetraedra(a, b, c, d, e, f):
        povrsina = 0
        povrsina += ploscina_trikotnika(a, b, c)
        povrsina += ploscina_trikotnika(a, e, f)
        povrsina += ploscina_trikotnika(b, d, f)
        povrsina += ploscina_trikotnika(c, d, e)
        return povrsina

.. doctest::

    >>> povrsina_tetraedra(896, 1073, 1073, 990, 1073, 1073)
    1816080.0


Stavek ``return``
-----------------

Tako kot drugje v Pythonu, se tudi stavki v telesu funkcije izvajajo od prvega
proti zadnjemu. Ko dosežemo stavek ``return``, funkcija pa vrne vrednost danega
izraza ter zaključi z izvajanjem. Tako tudi funkcija

.. testcode::

    def f(x):
        return x ** 2
        return 1000

vrne kvadrat števila ``x`` in ne števila 1000, saj se izvajanje ustavi ob
prvem stavku ``return``, zato do drugega sploh ne pride. Če stavka ``return``
ne napišemo, funkcija vrne posebno vrednost ``None``, ki označuje manjkajočo
vrednost. Pozorno se ji bomo posvetili kasneje, zaenkrat pa jo omenimo le zato,
da bomo znali razumeti spodnjo (precej pogosto) napako:

.. testcode::

    def g(x):
        x ** 2

.. doctest::

    >>> 2 * g(10)
    Traceback (most recent call last):
      ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'

Pričakovali bi, da bo rezultat klica ``2 * g(10)`` enak 200. Toda ker smo v
funkciji ``g`` pozabili na ``return``, je funkcija vrnila vrednost ``None``.
To lahko razberemo iz opozorila, v katerem približno piše, da operacije ``*`` ne
moremo uporabiti na celem številu in vrednosti ``None``. Vsakič, ko dobite
Vsakič, ko dobite podobno opozorilo (`TypeError`, v katerem se pojavlja
`NoneType`), posumite na to, da nekje manjka stavek ``return``.


Dokumentacijski niz
-------------------

Pred telesom funkcije dostikrat lahko zapišemo tudi  *dokumentacijski niz*
oziroma *docstring*. Ta niz ponavadi zapišemo med trojne enojne navednice, v
njem pa na kratko opišemo, kaj funkcija počne. Ta vrstica ni obvezna, je pa
koristna, saj lahko uporabnik, ki ne ve, kaj funkcija počne, to pogleda s
pomočjo funkcije ``help``.

.. testcode::

    import math

    def ploscina_trikotnika(a, b, c):
        '''Vrne ploščino trikotnika z danimi stranicami.'''
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


.. doctest::

    >>> help(ploscina_trikotnika)
    Help on function ploscina_trikotnika:
    <BLANKLINE>
    ploscina_trikotnika(a, b, c)
        Vrne ploščino trikotnika z danimi stranicami.
    <BLANKLINE>


Lokalnost spremenljivk
----------------------

Argumenti funkcije in spremenljivke, ki jih definiramo v telesu funkcije, se
izven funkcije ne vidijo. Pravimo, da so *lokalne*. Namen tega je, da funkcije
ne motijo ena druge s spremenljivkami, ki jih uporabljajo. Na primer, če
definiramo

.. testcode::

    def f(x):
        y = 3 * x
        return y

tedaj tudi po klicu funkcije ``f`` ne ``x`` ne ``y`` ne bosta definirana:

.. doctest::

    >>> f(4)
    12
    >>> x
    Traceback (most recent call last):
      ...
    NameError: name 'x' is not defined
    >>> y
    Traceback (most recent call last):
      ...
    NameError: name 'y' is not defined


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
        '''Vrne n-to Fibonaccijevo število.'''
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

Kaj se zgodi, če poskušate izračunati ``fibonacci(35)``? Po nekaj časa res dobite
pravilen odgovor 9227465, vendar to kaže, da nekaj ni v redu. Kmalu bomo videli
razloge, zakaj ta funkcija ni dobro napisana. Bolje bi bilo, če bi jo zastavili
malo drugače. Poleg Fibonaccijevega zaporedja, ki se začne s številoma 0 in 1,
obstajajo tudi splošno Fibonaccijevo zaporedje, ki se začne s poljubnima členoma
:math:`a` in :math:`b`:

.. math::

    a, b, a + b, b + (a + b) = a + 2 b, (a + b) + (a + 2 b) = 2 a + 3 b, \ldots

Vidimo, da je :math:`n`. člen tega zaporedja ravno :math:`n - 1`. člen zaporedja,
ki se začne s členoma :math:`b` in :math:`a + b`. Tedaj lahko definiramo:

.. testcode::

    def splosni_fibonacci(n, a, b):
        '''Vrne n-ti člen Fibonaccijevega zaporedja, ki se začne z a in b.'''
        if n == 0:
            return a
        elif n == 1:
            return b
        else:
            return splosni_fibonacci(n - 1, b, a + b)

Kot lahko sami preizkusimo, ta funkcija deluje veliko hitreje od prejšnje:

.. doctest::

    >>> splosni_fibonacci(35, 0, 1)
    9227465
    >>> splosni_fibonacci(25, 1, -1)
    -28657
    >>> splosni_fibonacci(25, 0, 2)
    150050
    >>> splosni_fibonacci(500, 0, 1)
    139423224561697880139724382870407283950070256587697307264108962948325571622863290691557658876222521294125

Pomembno ni torej samo to, da naš program pravilno izračuna iskani rezultat,
temveč tudi to, kako učinkovito ga izračuna.

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


Stavek ``assert``
-----------------

Tudi funkcija ``splosni_fibonacci`` še ni popolna. Kaj se zgodi, če pokličemo
``splosni_fibonacci(-2)``? Ker -2 ni enako ne 0 ne 1, bomo izvedli tretjo
vejo pogojnega stavka in izračunali ``splosni_fibonacci(-3, ...)``, iz tega
pa podobno ``splosni_fibonacci(-4, ...)`` in tako naprej, vse do trenutka, ko
se bo Python pritožil:

.. doctest::

    >>> splosni_fibonacci(-2)
    Traceback (most recent call last):
      ...
      File "...", line 8, in splosni_fibonacci
      File "...", line 8, in splosni_fibonacci
      File "...", line 8, in splosni_fibonacci
      File "...", line 8, in splosni_fibonacci
      File "...", line 8, in splosni_fibonacci
      File "...", line 8, in splosni_fibonacci
      File "...", line 3, in splosni_fibonacci
    RecursionError: maximum recursion depth exceeded in comparison

Pravi nam, da je naša rekurzija šla pregloboko. O tem bomo še bolj natančno
govorili, zaenkrat pa naj nam tako opozorilo pove, da smo program napisali tako,
da se ne bo ustavil. Da podobne situacije preprečimo, lahko uporabimo stavek
``assert``, v katerem napišemo pogoj, ki mu mora program zadoščati. Če mu ne,
Python javi napako.

.. testcode::

    def splosni_fibonacci(n, a=0, b=1):
        '''Vrne n-ti člen Fibonaccijevega zaporedja, ki se začne z a in b.'''
        assert n >= 0
        if n == 0:
            return a
        elif n == 1:
            return b
        else:
            return splosni_fibonacci(n - 1, b, a + b)

.. doctest::

    >>> splosni_fibonacci(-2)
    Traceback (most recent call last):
      ...
    AssertionError

Še vedno dobimo napako, vendar je ta bolj obvladljiva, pa še takoj se pojavi.
Stavke ``assert`` uporabljamo, kadar v nadaljevanju programa pričakujemo, da
je nekim pogojem zadoščeno. Namesto ``assert pogoj`` bi seveda lahko pisali tudi
nekaj v stilu:

.. code::

    if not pogoj:
        ustavi_program_in
        javi_napako

ampak ker je to pogosto koristno, so v ta namen uvedli ``assert``.
