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
pokličemo. Vsako vrstico telesa funkcije moramo zamakniti za štiri presledke, da se jasno vidi, kaj vse funkcija obsega. Prvo vrstico telesa smo
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
        return (
            ploscina_trikotnika(a, b, c)
            + ploscina_trikotnika(a, e, f)
            + ploscina_trikotnika(b, d, f)
            + ploscina_trikotnika(c, d, e)
        )

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


Dokumentacijski niz*
--------------------

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
