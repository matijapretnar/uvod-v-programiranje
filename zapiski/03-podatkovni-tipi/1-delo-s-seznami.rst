Delo s seznami
==============

Pisanje seznamov
----------------

Sename pišemo v oglatih oklepajih, med katerimi napišemo vrednosti, ločene z vejicami, na primer ``[10, 20, 30]`` je seznam, ki vsebuje tri števila, ``[]`` pa prazen seznam. Če želimo, lahko vejico pišemo tudi za zadnjim elementom. Seznami so lahko tudi gnezdeni. Na primer, matriko bi predstavili s seznamom seznamov:

.. testcode::

    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

V sezname lahko spravimo vrednosti različnih tipov, na primer:

.. testcode::

    [1, True, [2, 5], "Niz", 3.14]

Vendar običajno sezname uporabimo za predstavitev homogene zbirke podatkov, torej da so vse vrednosti istega tipa.



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

    >>> mat = [[5]]
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

