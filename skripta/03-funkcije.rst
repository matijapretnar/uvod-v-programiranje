Funkcije
========

Ploščino trikotnika s stranicami :math:`a, b, c` lahko izračunamo po Heronovi
formuli

.. math::
    \sqrt{s (s - a) (s - b) (s - c)}

kjer je :math:`s = (a + b + c) / 2`. Ploščino trikotnika s stranicami 4, 13 in 15
bi v Pythonu lahko torej izračunali s programom:

.. testcode::

    a, b, c = 4, 13, 15
    s = (a + b + c) / 2
    ploscina = (s * (s - a) * (s - b) * (s - c)) ** 0.5

Tedaj je

.. doctest::

    >>> ploscina
    24.0

Kako pa bi izračunali površino tetraedra, ki ima za lica štiri trikotnike?
Načeloma bi lahko pisali:

.. testcode::

    a, b, c, d, e, f = 896, 1073, 1073, 990, 1073, 1073
    s_abc = (a + b + c) / 2
    ploscina_abc = (s_abc * (s_abc - a) * (s_abc - b) * (s_abc - c)) ** 0.5
    s_aef = (a + e + f) / 2
    ploscina_aef = (s_aef * (s_aef - a) * (s_aef - e) * (s_aef - f)) ** 0.5
    s_bdf = (b + d + f) / 2
    ploscina_bdf = (s_bdf * (s_bdf - b) * (s_bdf - d) * (s_bdf - f)) ** 0.5
    s_cde = (c + d + e) / 2
    ploscina_cde = (s_cde * (s_cde - c) * (s_cde - d) * (s_cde - e)) ** 0.5
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
        '''Vrne ploščino trikotnika z danimi stranicami.'''
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

Oglejmo si njene sestavne dele. Vsaka definicija funkcije se začne s ključno
besedo ``def``, ki ji sledi ime funkcije, v našem primeru
``ploscina_trikotnika``, tej pa v oklepajih našteti argumenti, ki jih funkcija
sprejme. Funkcije lahko sprejmejo različno število argumentov. Naša sprejme tri
argumente, ki jih bomo shranili v spremenljivke ``a``, ``b`` in ``c``. V drugi
vrstici sledi za štiri presledke zamaknjeni *dokumentacijski niz* oziroma
*docstring*. Ta niz ponavadi zapišemo med trojne enojne navednice, v njem pa na
kratko opišemo, kaj funkcija počne. Ta vrstica ni obvezna, je pa koristna, saj
lahko uporabnik, ki ne ve, kaj funkcija počne, to pogleda s pomočjo funkcije
``help``.

.. doctest::

    >>> help(ploscina_trikotnika)
    Help on function ploscina_trikotnika:
    <BLANKLINE>
    ploscina_trikotnika(a, b, c)
        Vrne ploščino trikotnika z danimi stranicami.
    <BLANKLINE>

Nato sledi *telo funkcije*, torej ukazi, ki naj se izvedejo, ko funkcijo
pokličemo. Tako kot veje pogojnega stavka zamaknemo tudi celotno telo funkcije,
da se jasno vidi, kaj vse spada v definicijo funkcije. Tretjo vrstico smo že
videli, v četrti vrstici pa z ukazom ``return`` povemo, katero vrednost naj vrne
funkcija. Tako definirano funkcijo potem kličemo na enak način kot vgrajene
funkcije.

.. doctest::

    >>> ploscina_trikotnika(4, 13, 15)
    24.0

S pomočjo funkcije ``ploscina_trikotnika`` lahko tudi na veliko bolj pregleden
način zapišemo funkcijo za izračun površine tetraedra:

.. testcode::

    def povrsina_tetraedra(a, b, c, d, e, f):
        '''Vrne površino tetraedra z danimi stranicami.'''
        povrsina = 0
        povrsina += ploscina_trikotnika(a, b, c)
        povrsina += ploscina_trikotnika(a, e, f)
        povrsina += ploscina_trikotnika(b, d, f)
        povrsina += ploscina_trikotnika(c, d, e)
        return povrsina

.. doctest::

    >>> povrsina_tetraedra(896, 1073, 1073, 990, 1073, 1073)
    1816080.0

V telesu funkcij lahko pišemo poljubne stavke. Na primer, funkcijo, ki računa
absolutno vrednost, lahko s pomočjo pogojnega stavka napišemo kot:

.. testcode::

    def absolutna_vrednost(x):
        '''Vrne absolutno vrednost števila x.'''
        if x >= 0:
            return x
        else:
            return -x

.. doctest::

    >>> absolutna_vrednost(-5)
    5
    >>> absolutna_vrednost(3)
    3

Če veje ``else`` ne napišemo, se ob neresnični vrednosti ne zgodi nič. Na ta
način bi lahko funkcijo ``absolutna_vrednost`` definirali tudi kot:

.. testcode::

    def absolutna_vrednost(x):
        '''Vrne absolutno vrednost števila x.'''
        if x < 0:
            x *= -1
        return x

Torej, če je število negativno, ga pomnožimo z -1, preden ga vrnemo, sicer pa
ga vrnemo nespremenjenega.
