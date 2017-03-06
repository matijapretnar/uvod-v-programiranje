Seznami in nabori
=================

Če želimo delati z zaporedjem podatkov, uporabimo sezname.

Pisanje seznamov
----------------

Sename pišemo v oglatih oklepajih, med katerimi napišemo vrednosti, ločene z
vejicami, na primer ``[10, 20, 30]`` je seznam, ki vsebuje tri števila, ``[]``
pa prazen seznam. Če želimo, lahko vejico pišemo tudi za zadnjim elementom.
Seznami so lahko tudi gnezdeni. Na primer, matriko bi predstavili s seznamom
seznamov:

.. testcode::

    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

V sezname lahko spravimo vrednosti različnih tipov, na primer:

.. testcode::

    [1, True, [2, 5], "Niz", 3.14]

Vendar običajno sezname uporabimo za predstavitev homogene zbirke podatkov,
torej da so vse vrednosti istega tipa.



Operacije na seznamih
---------------------

Tako kot nize lahko tudi sezname stikamo z operacijo ``+`` in množimo s celimi števili:

.. doctest::

    >>> [10, 20, 30] + [6, 5, 4]
    [10, 20, 30, 6, 5, 4]
    >>> 4 * [1, 2]
    [1, 2, 1, 2, 1, 2, 1, 2]

Dolžino seznama dobimo s funkcijo ``len``:

.. doctest::

    >>> len([100, 200, 300])
    3
    >>> len([])
    0

Tudi na seznamih imamo na voljo predikata ``in`` in ``not in``, s katerima
ugotovimo, ali se nek element pojavlja v seznamu:

.. doctest::

    >>> 'Ema' in ['Ana', 'Bojan', 'Cvetka', 'David']
    False
    >>> 'Ana' in ['Ana', 'Bojan', 'Cvetka', 'David']
    True


.. testcode::

    def stevilo_dni(mesec, leto):
        if mesec == 2:
            return 29 if je_prestopno(leto) else 28
        elif mesec in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif mesec in [4, 6, 9, 11]:
            return 30


Indeksiranje in rezine
----------------------

Indeksiranje in rezine na seznamih delujejo tako kot na nizih:

.. doctest::

    >>> sez = [5, 3, 8, 2, 5, 2, 1, 2]
    >>> sez[0]
    5
    >>> sez[2]
    8
    >>> sez[len(sez) - 1]
    2
    >>> sez[-1]
    2
    >>> sez[:2]
    [5, 3]
    >>> sez[1:3]
    [3, 8]
    >>> sez[3:]
    [2, 5, 2, 1, 2]
    >>> sez[1:5:2]
    [3, 2]
    >>> sez[::2]
    [5, 8, 5, 1]

Če imamo gnezdene sezname, do elementov dostopamo z gnezdenimi indeksi:

    >>> mat = [[1, 0, 0], [0, -1, 2], [3, 1, 5]]
    >>> mat[0][0]
    1
    >>> mat[1][-1]
    2

Na primer, sled matrike bi lahko izračunali kot:

.. testcode::

    def sled(matrika):
        '''Izračuna sled dane matrike.'''
        vsota_diagonalnih = 0
        for i in range(len(matrika)):
            vsota_diagonalnih += matrika[i][i]
        return vsota_diagonalnih

.. doctest::

    >>> sled(mat)
    5

Sledi pa nikakor ne bomo izračunali na sledeči (pri študentih dostikrat videni)
način:

.. testcode::

    def grozna_sled(matrika):
        '''Na popolnoma napačen izračuna sled dane matrike.'''
        vsota_diagonalnih = 0
        for i in range(len(matrika)):
            for j in range(len(matrika)):
                if i == j:
                    vsota_diagonalnih += matrika[i][j]
        return vsota_diagonalnih

Funkcija sled matrike sicer izračuna pravilno, vendar na izjemno potraten način,
saj se sprehodi čez celotno matriko, ne le čez diagonalne elemente. Na primer,
pri matriki velikosti :math:`1000 \times 1000` bi druga funkcija pregledala
tisočkrat več elementov (in posledično porabila tisočkrat več časa).


Zanka ``for`` na seznamih
-------------------------

Tako kot se lahko z zanko ``for`` sprehodimo po vseh znakih v nizu, se lahko
z njo sprehodimo tudi po vseh elementih danega seznama:

.. testcode::

    def vsota_elementov(seznam):
        '''Vrne vsoto elementov v danem seznamu.'''
        vsota = 0
        for trenutni in seznam:
            vsota += trenutni
        return vsota

.. doctest::

    >>> vsota_elementov([10, 2, 4000, 300])
    4312

Največji element v danem seznamu lahko poiščemo tako, da zaporedoma vsak element
seznama primerjamo z do sedaj največjim videnim elementom. Če je trenutni element
večji, do sedaj največji element popravimo. Ko pregledamo vse elemente v seznamu,
je do sedaj največji element tudi na splošno največji element. Edina stvar, na
katero moramo še paziti, je ta, da na začetku izberemo ustrezen največji element.
Tu imamo dve dobri izbiri. (Slaba izbira bi bila, da bi za največji do zdaj
viden element vzeli neko dovolj majhno število, na primer 0 ali -9999999 – ta
izbira je očitno napačna!) Prva dobra izbira je kar prvi element v seznamu,
pri čemer moramo potem poprej preveriti še to, da je seznam neprazen:

.. testcode::

    def najvecji_element(seznam):
        '''Vrne največji element v danem seznamu. Če ga ni, vrne None'''
        if len(seznam) == 0:
            return
        najvecji_do_zdaj = seznam[0]
        for trenutni in seznam:
            if trenutni > najvecji_do_zdaj:
                najvecji_do_zdaj = trenutni
        return najvecji_do_zdaj

Druga izbira pa je ``None``, vendar moramo potem pri vsaki primerjavi pogledati,
ali imamo že “pravi” največji element ali je to do sedaj še vedno ``None``:

.. testcode::

    def najvecji_element(seznam):
        '''Vrne največji element v danem seznamu. Če ga ni, vrne None'''
        najvecji_do_zdaj = None
        for trenutni in seznam:
            if najvecji_do_zdaj == None or trenutni > najvecji_do_zdaj:
                najvecji_do_zdaj = trenutni
        return najvecji_do_zdaj


.. doctest::

    >>> najvecji_element([10, 2, 4000, 300])
    4000

Seveda lahko uporabimo tudi vgrajene funkcije:

.. doctest::

    >>> sum([10, 2, 4000, 300])
    4312
    >>> min([10, 2, 4000, 300])
    2
    >>> max([10, 2, 4000, 300])
    4000



Izpeljani seznami
-----------------

Python omogoča, da sezname tvorimo na enostaven način z **izpeljanimi seznami**,
ki so oblike ``[izraz for spremenljivka in mozne_vrednosti]``, podobno kot v
matematiki množice pišemo kot :math:`\{ 2 \cdot n \mid n \in \{1, \dots, 9\}\}`:

.. doctest::

    >>> [2 * n for n in range(1, 10)]
    [2, 4, 6, 8, 10, 12, 14, 16, 18]
    >>> potence = [2 ** n for n in range(10)]
    >>> potence
    [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    >>> [n - 1 for n in potence]
    [0, 1, 3, 7, 15, 31, 63, 127, 255, 511]
    >>> [int(stevka) for stevka in str(3141592)]
    [3, 1, 4, 1, 5, 9, 2]
    
Če želimo, lahko v izpeljani seznamih oblike
``[izraz for spremenljivka in mozne_vrednosti if pogoj]``
s pogojem določimo, katere elemente želimo:

.. doctest::

    >>> [2 * n for n in range(1, 10) if n % 3 == 1]
    [2, 8, 14]


Spreminanje in brisanje elementov
---------------------------------

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


Spreminjamo lahko tudi celotne rezine:

.. doctest::

    >>> sez[1:3]
    [3, 8]
    >>> sez[1:3] = [100, 300]
    >>> sez
    [5, 100, 300, 200, 5, 1, 500]

Če nadomestna rezina ni enake dolžine kot prvotna, se seznam ustrezno skrajša
ali podaljša

.. doctest::

    >>> sez[2:5] = []
    >>> sez
    [5, 100, 1, 500]
    >>> sez[2:2] = [0, 0, 0]
    >>> sez
    [5, 100, 0, 0, 0, 1, 500]

Kot vidimo, lahko nadomestimo tudi prazno rezino, s čimer nove elemente vrinemo
v seznam. Nadomeščanje prazne rezine ni isto kot nadomeščanje elementa z
istim indeksom kot rezina:

.. doctest::

    >>> sez[2] = [20, 20, 20]
    >>> sez
    [5, 100, [20, 20, 20], 0, 0, 1, 500]

Tudi rezine lahko brišemo:

.. doctest::

    >>> del sez[1:4]
    >>> sez
    [5, 0, 1, 500]

Pri spreminjanju seznamov je treba biti previden, saj ne deluje tako, kot
smo navajeni pri spreminjanju vrednosti spremenljivk. Na primer, pišimo

.. doctest::

    >>> a = 5
    >>> b = a
    >>> a = 0
    >>> b
    5

Vidimo, da se vrednost spremenljivke ``b`` ni spremenila, saj smo jo v drugi
vrstici nastavili na število 5. Pri seznamih je stvar malo drugačna. Če pišemo

.. doctest::

    >>> a = [1, 2, 3]
    >>> b = a
    >>> a = []
    >>> b
    [1, 2, 3]

so stvari še vedno take, kot bi jih pričakovali. Vrednost ``b`` smo nastavili
na isti seznam kot ``a``, vendar smo potem rekli, da naj bo v ``a`` shranjen
drugačen seznam, s čimer na vrednost v ``b`` nismo vplivali. Če pa pišemo

.. doctest::

    >>> a = [1, 2, 3]
    >>> b = a
    >>> a[1] = 20
    >>> b
    [1, 20, 3]

se je s tem, ko smo spremenili ``a``, spremenil tudi ``b``. Kaj se je zgodilo?
Ko smo napisali ``b = a``, smo povedali, naj bo v ``b`` shranjen isti seznam
kot ``a``. In z ``a[1] = 20`` smo povedali, naj se na mesto ``1`` v seznamu,
shranjenem v ``a``, zapiše 20. Ker je v ``b`` shranjen isti (ne le enak) seznam
kot v ``a``, je s tem tudi seznam v ``b`` drugačen.

Pogosta past, v katero se na začetku ujamemo zaradi spremenljivosti seznamov,
je izračun identične matrike. Vemo že, da lahko v Pythonu seznam pomnožimo s
številom:


.. doctest::

    >>> 3 * [0]
    [0, 0, 0]

To nam da idejo, da bi lahko na isti način izračunali ničelno matriko:

.. doctest::

    >>> 3 * [3 * [0]]
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

Izračun je videti pravilen, vendar vse tri vrstice te matrike kažejo na isti
seznam. To je tako, kot če bi pisali:

.. doctest::

    >>> vrstica = [0, 0, 0]
    >>> matrika = [vrstica, vrstica, vrstica]

Poskusimo iz te matrike dobiti identično matriko tako, da po diagonali nastavimo
enice. Najprej nastavimo prvi element v prvi vrstici:

.. doctest::

    >>> matrika[0][0] = 1
    >>> matrika
    [[1, 0, 0], [1, 0, 0], [1, 0, 0]]

Kaj se je zgodilo? Ker druga in tretja vrstica kažeta na isti seznam kot prva,
smo tudi v njima prvi element popravili na 1. Če sedaj nastavimo še drugi
element v drugi vrstici in tretjega v tretji vrstici se zgodba ponovi:

.. doctest::

    >>> matrika[1][1] = 1
    >>> matrika[2][2] = 1
    >>> matrika
    [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

Če želimo identično matriko izračunati na pravilen način, moramo za predstavitev
vsake vrstice podati svoj seznam, zato ne moremo uporabiti le pomnoževanja
seznamov. Namesto tega lahko uporabimo izpeljani seznam:

.. testcode::

    def identicna_matrika(n):
        '''Vrne identično matriko velikosti n x n.'''
        matrika = [n * [0] for _ in range(n)]
        for k in range(len(matrika)):
            matrika[k][k] = 1
        return matrika

.. doctest::

    >>> identicna_matrika(3)
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]]


Metode na seznamih
------------------

Za večino pogosto uporabljanih stvari na seznamih obstajajo že vgrajene metode.
Te povečini ne vračajo ničesar, temveč le spremenijo dani seznam. Izjemi sta
metodi ``index`` in ``count``, ki vrneta vrednost in seznam pustita pri miru, ter
metoda ``pop`` ki tako spremeni seznam kot vrne vrednost.

* ``sez.append(x)``
    Dodaj element `x` na konec seznama ``sez``.

* ``sez.extend(sez2)``
    Na konec seznama ``sez`` dodaj vse elemente iz seznama ``sez2``.

* ``sez.insert(i, x)``
    Pred element na mestu ``i`` v seznamu ``sez`` vstavi element ``x``.

* ``sez.remove(x)``
    Iz seznama ``sez`` odstrani prvo pojavitev vrednosti ``x``.

* ``sez.pop(i=-1)``
    Vrni element na mestu ``i`` v seznamu ``sez`` in odstrani ta element iz seznama.
    Če indeksa ``i`` ne podamo, metoda odstrani zadnji element.

* ``sez.clear()``
    Iz seznama ``sez`` pobriši vse elemente.

* ``sez.index(x)``
    Vrni prvo mesto, na katerem se v seznamu ``sez`` nahaja vrednost ``x``.

* ``sez.count(x)``
    Vrni število pojavitev vrednosti ``x`` v seznamu ``sez``.

* ``sez.sort(key=None, reverse=False)``
    Na mestu uredi seznam glede na vrednosti funkcije ``key``. Če parameter
    ``reverse`` nastavimo na ``True``, bo seznam urejen padajoče.

* ``sez.reverse()``
    Obrni seznam ``sez`` na glavo.

Primer uporabe:

.. doctest::

    >>> sez = [66.25, 333, 333, 1, 1234.5]
    >>> (sez.count(333), sez.count(66.25), sez.count('x'))
    (2, 1, 0)
    >>> sez.insert(2, -1)
    >>> sez.append(333)
    >>> sez
    [66.25, 333, -1, 333, 1, 1234.5, 333]
    >>> sez.index(333)
    1
    >>> sez.remove(333)
    >>> sez
    [66.25, -1, 333, 1, 1234.5, 333]
    >>> sez.reverse()
    >>> sez
    [333, 1234.5, 1, 333, -1, 66.25]
    >>> sez.sort()
    >>> sez
    [-1, 1, 66.25, 333, 333, 1234.5]
    >>> sez.pop()
    1234.5
    >>> sez
    [-1, 1, 66.25, 333, 333]

Metodo ``append`` pogosto uporabljamo za izračun seznama ustreznih elementov.
To storimo tako, da ustvarimo prazen seznam, nato pa vanj z metodo ``append``
dodamo vsak ustrezen element. To je podoben postopek kot pri izračunu vsote
ustreznih elementov, kjer smo ustvarili spremenljivko z začetno vrednostjo 0,
nato pa ji prištevali ustrezne elemente.

.. testcode::

    def vsota_pozitivnih_elementov(seznam):
        '''Vrne vsoto vseh pozitivnih elementov danega seznama.'''
        vsota = 0
        for element in seznam:
            if element > 0:
                vsota += element
        return vsota

    def pozitivni_elementi(seznam):
        '''Vrne seznam vseh pozitivnih elementov danega seznama.'''
        pozitivni = []
        for element in seznam:
            if element > 0:
                pozitivni.append(element)
        return pozitivni


.. doctest::

    >>> vsota_pozitivnih_elementov([1, -5, 2, 3])
    6
    >>> pozitivni_elementi([1, -5, 2, 3])
    [1, 2, 3]

Seveda bi obe funkciji lepše napisali s pomočjo izpeljanih seznamov:

.. testcode::

    def pozitivni_elementi(seznam):
        '''Vrne seznam vseh pozitivnih elementov danega seznama.'''
        return [element for element in seznam if element > 0]

    def vsota_pozitivnih_elementov(seznam):
        '''Vrne seznam vseh pozitivnih elementov danega seznama.'''
        return sum([element for element in seznam if element > 0])
        # ali pa kar
        # return sum(pozitivni_elementi(seznam))


Nabori
------

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


``zip`` in ``enumerate``
------------------------

Dostikrat želimo hkrati dostopati do elementov seznama in njihovih indeksov.

Predstavimo polinome s seznamom koeficientov, urejenim od prostega proti
vodilnemu členu. Polinom :math:`3 - x^2` bi tako predstavili s seznamom
``[3, 0, -1]``. Pri izračunu vrednosti polinoma želimo hkrati dostopati tako do
koeficientov kot do njihovih indeksov, ki ustrezajo potenci. To lahko storimo
na več načinov. Lahko se vozimo po indeksih in prek njih dostopamo do
koeficientov:

.. testcode::

    def vrednost_polinoma(koeficienti, tocka):
        '''Vrne vrednost polinoma z danimi koeficienti v dani točki.'''
        vsota = 0
        for i in range(len(koeficienti)):
            koeficient = koeficienti[i]
            vsota += koeficient * tocka ** i
        return vsota


.. doctest::

    >>> vrednost_polinoma([3, 0, 1], 1)
    4
    >>> vrednost_polinoma([3, 0, 1], 2)
    7

Lahko se vozimo po koeficientih in hkrati povečujemo števec indeksa:

.. testcode::

    def vrednost_polinoma(koeficienti, tocka):
        '''Vrne vrednost polinoma z danimi koeficienti v dani točki.'''
        vsota = 0
        i = 0
        for koeficient in koeficienti:
            vsota += koeficient * tocka ** i
            i += 1
        return vsota

Najbolj enostavno pa je, da uporabimo funkcijo ``enumerate``, ki vrne zaporedje
parov, v katerih so druge komponente vrednosti danega seznama, prve komponente
pa njihovi indeksi:

 .. doctest::
 
     >>> list(enumerate([20, 200, 2000]))
     [(0, 20), (1, 200), (2, 2000)]
     >>> list(enumerate('beseda'))
     [(0, 'b'), (1, 'e'), (2, 's'), (3, 'e'), (4, 'd'), (5, 'a')]

S pomočjo funkcije ``enumerate`` lahko vrednost polinoma izračunamo kot:

.. testcode::

    def vrednost_polinoma(koeficienti, tocka):
        '''Vrne vrednost polinoma z danimi koeficienti v dani točki.'''
        vsota = 0
        for i, koeficient in enumerate(koeficienti):
            vsota += koeficient * tocka ** i
        return vsota

Kot vidimo, lahko tudi v zanki ``for`` uporabimo razstavljanje naborov, in
pare, ki nam jih podaja ``enumerate``, takoj shranimo v dve spremenljivki.

.. caution::

    Paziti moramo, da indeksa ne računamo s pomočjo metode ``.index``, saj
    je ta način prvič neučinkovit, drugič pa ne bi vedno delovala pravilno, saj
    ``.index`` vrne indeks prve pojavitve iskane vrednosti:


    .. testcode::

        def napacna_vrednost_polinoma(koeficienti, tocka):
            '''Vrne vrednost polinoma z danimi koeficienti v dani točki.'''
            vsota = 0
            for koeficient in koeficienti:
                i = koeficienti.index(koeficient)
                vsota += koeficient * tocka ** i
            return vsota

    .. doctest::

        >>> vrednost_polinoma([0, 2, 0, 2], 3)
        60
        >>> napacna_vrednost_polinoma([0, 2, 0, 2], 3)
        12

    Ker je v spodnjem klicu funkcije metoda ``.index`` za indeks prve pojavitve
    vrednosti 2 obakrat vrnila 1, je funkcija vrnila :math:`2 \cdot 3^1 + 2 \cdot 3^1 = 6`
    namesto :math:`2 \cdot 3^1 + 2 \cdot 3^3 = 60`.


Podobno kot ``enumerate`` deluje funkcija ``zip``, ki sprejme več seznamov,
vrne pa zaporedje naborov istoležnih elementov:

.. doctest::

    >>> list(zip([10, 20, 30], [4, 5, 6]))
    [(10, 4), (20, 5), (30, 6)]
    >>> list(zip([10, 20, 30], [4, 5, 6], 'abc'))
    [(10, 4, 'a'), (20, 5, 'b'), (30, 6, 'c')]

Funkciji se reče ``zip``, ker združuje elemente različnih seznamov tako, kot
zadrga. Vrnjeno zaporedje ima toliko elementov, kot najkrajši argument funkcije:

    >>> list(zip([10, 20, 30], [4, 5, 6], 'ab'))
    [(10, 4, 'a'), (20, 5, 'b')]

S pomočjo funkcije ``zip`` lahko enostavno izračunamo skalarni produkt:

.. testcode::

    def skalarni_produkt(vektor1, vektor2):
        '''Vrne skalarni produkt dveh vektorjev iste dimenzije.'''
        assert len(vektor1) == len(vektor2)
        vsota = 0
        for x1, x2 in zip(vektor1, vektor2):
            vsota += x1 * x2
        return vsota


.. doctest::

    >>> skalarni_produkt([1, -2, 5], [-2, 5, 2])
    -2


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

S pomočjo vzorca za preostale argumente bi tako funkcijo napisali tako, da bi
najprej preverili, koliko argumentov smo dobili, nato pa ustrezno poiskali
maksimum:

.. testcode::

    def maksimum(*argumenti):
        '''
        Ob več argumentih vrne največjega.
        Ob enem argumentu vrne njegov največji element.
        '''
        if len(argumenti) == 0:       # Če nismo dobili nobenega argumenta,
            return None               # vrnemo None.
        if len(argumenti) == 1:       # Če smo dobili en argument,
            kandidati = argumenti[0]  # iščemo maksimum med njegovimi elementi.
        else:                         # Če smo dobili več argumentov,
            kandidati = argumenti     # iščemo maksimum med njimi.

        # Uporabimo znan postopek za iskanje največjega elementa.
        najvecji = None
        for kandidat in kandidati:
            if najvecji is None or najvecji < kandidat:
                najvecji = kandidat
        return najvecji


.. doctest::

    >>> maksimum([3, 5], [4, 1])
    [4, 1]
    >>> maksimum([3, 5, 4, 1])
    5
    >>> maksimum(3, 5, 4, 1)
    5
