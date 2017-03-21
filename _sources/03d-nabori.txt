Nabori
======

Nabori se obnašajo podobno kot seznami, le da njihovih vrednosti ne moremo
spreminjati. Pišemo jih tako kot sezname, le med običajne oklepaje: ``(1, 2, 3)``.
Nabor z enim elementom pišemo kot ``(1, )`` (razmislite, zakaj ga ne pišemo kot
``(1)``). Včasih lahko nabore pišemo kar brez oklepajev:


.. doctest::

    >>> 1, 2, 3
    (1, 2, 3)
    

Druga razlika pa je ta, da so nabori običajno heterogeni: elementi na različnih
mestih imajo lahko različne tipe in različne pomene:

.. testcode::

    student = ('Ana', 'Novak', 27162315)
    ucenci = ['Ana', 'Bojan', 'Cvetka', 'David']
    datum = (30, 'marec', 2016)
    datumi = [(30, 'marec', 2016), (1, 'april', 2016), (25, 'junij', 2016)]

Sicer za nabore veljajo podobne lastnosti: lahko jih stikamo in množimo; lahko
izračunamo njihovo vsoto, minimum, maksimum in dolžino; s predikatom ``in``
lahko pogledamo, ali vsebujejo dani element; lahko jih indeksiramo in delamo
rezine; po njih se lahko sprehodimo z zanko ``for``; od metod pa sta na voljo le
``count`` in ``index``, saj ti dve edini ne spreminjata ničesar.

Razstavljanje naborov
---------------------

Kljub temu, da lahko do elementov nabora dostopamo z indeksi, je pogosto
uporabno, da jih razstavimo. To storimo s hkratnim prireditvenim stavkom, v
katerem na levi strani naštejemo več spremenljivk, na desni pa podamo nabor, ki
ga želimo razstaviti:

.. doctest::

    >>> datum = (30, 'marec', 2016)
    >>> dan, mesec, leto = datum
    >>> dan
    30
    >>> mesec
    'marec'

V resnici gre pri hkratnih prireditvenih stavkih za sestavljanje in razstavljanje
naborov. Pri razstavljanju je treba paziti, da je število spremenljivk na levi
enako dolžini nabora na desni, saj v nasprotnem primeru pride do napake.


Razstavljanje seznamov
----------------------

Na podoben način kot nabore lahko razstavljamo tudi sezname:

.. doctest::

    >>> prvi, drugi, tretji = [10, 20, 30]
    >>> prvi
    10
    >>> tretji
    30

Toda seznami običajno nimajo definirane dolžine, zato lahko pri njihovem
razstavljanju uporabimo tudi poseben vzorec, ki v spremenljivko shrani vse
preostale elemente:

.. doctest::

    >>> prvi, drugi, *ostali = [10, 20, 30, 40, 50, 60, 70]
    >>> prvi
    10
    >>> drugi
    20
    >>> ostali
    [30, 40, 50, 60, 70]

Vzorec za preostale elemente se lahko pojavi tudi kje drugje kot na koncu:

.. doctest::

    >>> prvi, *ostali, predzadnji, zadnji = [10, 20, 30, 40, 50, 60, 70]
    >>> prvi
    10
    >>> ostali
    [20, 30, 40, 50]
    >>> predzadnji
    60
    >>> zadnji
    70

Vseeno pa vzorec za preostale elemente lahko uporabimo največ enkrat:

.. doctest::

    >>> *prva_polovica, *druga_polovica = [1, 2, 3, 4]
    Traceback (most recent call last):
      ...
    SyntaxError: two starred expressions in assignment

Na podoben način lahko razstavljamo tudi nabore, nize in ostale strukture,
po katerih se lahko sprehajamo z zanko ``for``, vendar bo v spremenljivki
vedno shranjen seznam preostalih elementov:

.. doctest::

    >>> zacetnica, *ostale_crke = 'abrakadabra'
    >>> zacetnica
    'a'
    >>> ostale_crke
    ['b', 'r', 'a', 'k', 'a', 'd', 'a', 'b', 'r', 'a']
    >>> prvi_par, *ostali_pari = enumerate('balon')
    >>> prvi_par
    (0, 'b')
    >>> ostali_pari
    [(1, 'a'), (2, 'l'), (3, 'o'), (4, 'n')]


Vzorec za preostale elemente lahko uporabimo tudi v definicijah funkcij:

.. testcode::

    def vrni_zadnji_argument(*args):
        return args[-1]


.. doctest::

    >>> vrni_zadnji_argument(10, 20, 30)
    30
    >>> vrni_zadnji_argument(1)
    1

Tak vzorec na primer uporablja funkcija ``max`` (in njej podobne). Ta funkcija
namreč deluje tako, da v primeru, ko dobi en argument, vrne njegov največji
element, ko pa dobi več argumentov, pa vrne največjega:


.. doctest::

    >>> max([3, 5], [4, 1])
    [4, 1]
    >>> max([3, 5, 4, 1])
    5
    >>> max(3, 5, 4, 1)
    5

