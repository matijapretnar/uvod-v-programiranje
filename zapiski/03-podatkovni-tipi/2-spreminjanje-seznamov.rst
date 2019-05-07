Spreminjanje seznamov
=====================

Spreminanje posameznih elementov
--------------------------------

Za razliko od nizov lahko vrednosti v seznamih tudi spreminjamo:

.. doctest::

    >>> sez = [5, 3, 8, 2, 5, 7, 1, 2]
    >>> sez[3] = 200
    >>> sez
    [5, 3, 8, 200, 5, 7, 1, 2]
    >>> sez[-1] = 500
    >>> sez
    [5, 3, 8, 200, 5, 7, 1, 500]


Vrednosti lahko tudi brišemo

.. doctest::

    >>> del sez[5]
    >>> sez
    [5, 3, 8, 200, 5, 1, 500]


Spreminjanje rezin
------------------

Spreminjamo lahko tudi celotne rezine:

.. doctest::

    >>> sez[1:3]
    [3, 8]
    >>> sez[1:3] = [100, 300]
    >>> sez
    [5, 100, 300, 200, 5, 1, 500]

Če nadomestna rezina ni enake dolžine kot prvotna, se seznam ustrezno skrajša ali podaljša

.. doctest::

    >>> sez[2:5] = []
    >>> sez
    [5, 100, 1, 500]
    >>> sez[2:2] = [0, 0, 0]
    >>> sez
    [5, 100, 0, 0, 0, 1, 500]

Kot vidimo, lahko nadomestimo tudi prazno rezino, s čimer nove elemente vrinemo v seznam. Nadomeščanje prazne rezine ni isto kot nadomeščanje elementa z istim indeksom kot rezina:

.. doctest::

    >>> sez[2] = [20, 20, 20]
    >>> sez
    [5, 100, [20, 20, 20], 0, 0, 1, 500]

Tudi rezine lahko brišemo:

.. doctest::

    >>> del sez[1:4]
    >>> sez
    [5, 0, 1, 500]

Previdnost pri spreminjanju seznamov
------------------------------------

Pri spreminjanju seznamov je treba biti previden, saj ne deluje tako, kot smo navajeni pri spreminjanju vrednosti spremenljivk. Na primer, pišimo

.. doctest::

    >>> a = 5
    >>> b = a
    >>> a = 0
    >>> b
    5

Vidimo, da se vrednost spremenljivke ``b`` ni spremenila, saj smo jo v drugi vrstici nastavili na število 5. Pri seznamih je stvar malo drugačna. Če pišemo

.. doctest::

    >>> a = [1, 2, 3]
    >>> b = a
    >>> a = []
    >>> b
    [1, 2, 3]

so stvari še vedno take, kot bi jih pričakovali. Vrednost ``b`` smo nastavili na isti seznam kot ``a``, vendar smo potem rekli, da naj bo v ``a`` shranjen drugačen seznam, s čimer na vrednost v ``b`` nismo vplivali. Če pa pišemo

.. doctest::

    >>> a = [1, 2, 3]
    >>> b = a
    >>> a[1] = 20
    >>> b
    [1, 20, 3]

se je s tem, ko smo spremenili ``a``, spremenil tudi ``b``. Kaj se je zgodilo? Ko smo napisali ``b = a``, smo povedali, naj bo v ``b`` shranjen isti seznam kot ``a``. In z ``a[1] = 20`` smo povedali, naj se na mesto ``1`` v seznamu, shranjenem v ``a``, zapiše 20. Ker je v ``b`` shranjen isti (ne le enak) seznam kot v ``a``, je s tem tudi seznam v ``b`` drugačen.

Pogosta past, v katero se na začetku ujamemo zaradi spremenljivosti seznamov, je izračun identične matrike. Vemo že, da lahko v Pythonu seznam pomnožimo s številom:


.. doctest::

    >>> 3 * [0]
    [0, 0, 0]

To nam da idejo, da bi lahko na isti način izračunali ničelno matriko:

.. doctest::

    >>> 3 * [3 * [0]]
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

Izračun je videti pravilen, vendar vse tri vrstice te matrike kažejo na isti seznam. To je tako, kot če bi pisali:

.. doctest::

    >>> vrstica = [0, 0, 0]
    >>> matrika = [vrstica, vrstica, vrstica]

Poskusimo iz te matrike dobiti identično matriko tako, da po diagonali nastavimo enice. Najprej nastavimo prvi element v prvi vrstici:

.. doctest::

    >>> matrika[0][0] = 1
    >>> matrika
    [[1, 0, 0], [1, 0, 0], [1, 0, 0]]

Kaj se je zgodilo? Ker druga in tretja vrstica kažeta na isti seznam kot prva, smo tudi v njima prvi element popravili na 1. Če sedaj nastavimo še drugi element v drugi vrstici in tretjega v tretji vrstici se zgodba ponovi:

.. doctest::

    >>> matrika[1][1] = 1
    >>> matrika[2][2] = 1
    >>> matrika
    [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

Če želimo identično matriko izračunati na pravilen način, moramo za predstavitev vsake vrstice podati svoj seznam, zato ne moremo uporabiti le pomnoževanja seznamov.
