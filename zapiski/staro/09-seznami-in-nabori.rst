Izpeljani seznami
-----------------

Python omogoča, da sezname tvorimo na enostaven način z **izpeljanimi seznami**, ki so oblike ``[izraz for spremenljivka in mozne_vrednosti]``, podobno kot v matematiki množice pišemo kot :math:`\{ 2 \cdot n \mid n \in \{1, \dots, 9\}\}`:
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
    
Če želimo, lahko v izpeljani seznamih oblike ``[izraz for spremenljivka in mozne_vrednosti if pogoj]`` s pogojem določimo, katere elemente želimo:

.. doctest::

    >>> [2 * n for n in range(1, 10) if n % 3 == 1]
    [2, 8, 14]



Metode na seznamih
------------------

Za večino pogosto uporabljanih stvari na seznamih obstajajo že vgrajene metode. Te povečini ne vračajo ničesar, temveč le spremenijo dani seznam. Izjemi sta metodi ``index`` in ``count``, ki vrneta vrednost in seznam pustita pri miru, ter metoda ``pop`` ki tako spremeni seznam kot vrne vrednost.

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

Metodo ``append`` pogosto uporabljamo za izračun seznama ustreznih elementov. To storimo tako, da ustvarimo prazen seznam, nato pa vanj z metodo ``append`` dodamo vsak ustrezen element. To je podoben postopek kot pri izračunu vsote ustreznih elementov, kjer smo ustvarili spremenljivko z začetno vrednostjo 0, nato pa ji prištevali ustrezne elemente.

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
