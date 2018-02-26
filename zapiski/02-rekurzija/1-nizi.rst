Nizi
====

V programih seveda ne delamo le s števili, temveč tudi z drugimi podatki, na primer besedili. V ta namen Python podpira nize, ki so strnjena zaporedja znakov.

Operacije na nizih
------------------

Nize običajno pišemo v enojnih narekovajih, na primer ``'to je primer niza'``. Nize lahko stikamo z operacijo ``+`` in množimo s celimi števili:

.. doctest::

    >>> 'Dober' + 'dan'
    'Doberdan'
    >>> 10 * 'ha'
    'hahahahahahahahahaha'
    >>> 'tro' + 4 * 'lo'
    'trololololo'

Dolžino niza dobimo s funkcijo ``len``:

.. doctest::

    >>> len('lokomotiva')
    10
    >>> len('')
    0

Nize lahko med seboj tudi primerjamo. Pri tem Python nize ureja leksikografsko, torej tako, kot bi bili urejeni v leksikonu ali kazalu: najprej primerja prvi črki, če sta ti dve enaki, pogleda drugi dve, in tako naprej. Pri tem velike črke pridejo na vrsto pred malimi, na šumnike pa se brez posebnih knjižnic Python ne spozna.

.. doctest::

    >>> 'beseda' == 'konj'
    False
    >>> 'abak' <= 'abeceda'
    True
    >>> 'Z' <= 'a'
    True
    >>> 'd' >= 'č'
    False

Na nizih imamo na voljo tudi predikat ``in``, s katerim ugotovimo, ali se nek niz pojavlja kot podniz v drugem nizu. Na voljo je tudi ``not in``, s katerim bolj berljivo zapišemo ravno nasprotno stvar:

.. doctest::

    >>> 'gram' in 'Uvod v programiranje'
    True
    >>> 'liter' in 'Uvod v programiranje'
    False
    >>> not ('liter' in 'Uvod v programiranje')
    True
    >>> 'liter' not in 'Uvod v programiranje'
    True


Zapis nizov
-----------

Nize lahko pišemo tudi z dvojnimi narekovaji, ki jih ponavadi uporabimo takrat, kadar v nizu želimo uporabiti enojni narekovaj: ``"Tole je kr'neki!"``. V tem primeru niza ne moremo pisati med enojnimi narekovaji, saj bi Python po narekovaju za ``kr`` mislil, da je konec niza.

Včasih želimo uporabiti obe vrsti narekovajev. V tem primeru si pomagamo z *ubežnimi znaki*. To so znaki, ki jih na običajni način ne moremo zapisati, zato uporabimo poseben zapis, ki se začne z znakom ``\``. Tedaj lahko pišemo ``'"Tole je kr\'neki," je rekla.'`` ali pa ``"\"Tole je kr'neki,\" je rekla."``. Ubežne znake brez težav lahko pišemo tudi tedaj, kadar ni treba ``'\"Grem v rudnik,\" je rekla.'``. Z ubežnimi znaki lahko zapišemo tudi znak za novo vrstico ``\n``, za tabulator ``\t`` in seveda tudi za poševnico ``\\``, saj je ne moremo pisati le kot ``\``, ker bi Python to razumel kot začetek ubežnega znaka.

Nize lahko pišemo tudi med tri enojne (``'''``) ali tri dvojne (``"""``) narekovaje. V tem primeru za en sam narekovaj ne potrebujemo ubežnega znaka. Take nize lahko pišemo tudi čez več vrstic.

Indeksiranje
------------

Do posameznega znaka v nizu pridemo z *indeksi*. Z izrazom ``niz[i]`` dostopamo do ``i``-tega znaka v danem nizu:

.. doctest::

    >>> 'rekurzija'[3]
    'u'
    >>> 'rekurzija'[0]
    'r'
    >>> 'rekurzija'[-1]
    'a'

Indeksi se začnejo šteti z 0. Če uporabimo negativna števila, lahko štejemo tudi od zadaj, vendar tam začnemo šteti z -1 (saj je -0 = 0).

.. code::

     0   1   2   3   4   5   6   7   8
     R   E   K   U   R   Z   I   J   A
    -9  -8  -7  -6  -5  -4  -3  -2  -1

Rezine
------

Na podoben način lahko dostopamo tudi do podnizov. Če napišemo ``niz[i:j]`` bomo dobili niz, ki mu pravimo *rezina* in sega od vključno ``i``-tega do vključno ``j - 1``-tega znaka. Če kakšno od meja izpustimo, bomo vzeli vse znake od začetka oziroma do konca.

.. doctest::

    >>> 'rekurzija'[2]
    'k'
    >>> 'rekurzija'[6]
    'i'
    >>> 'rekurzija'[2:6]
    'kurz'
    >>> 'rekurzija'[:6]
    'rekurz'
    >>> 'rekurzija'[2:]
    'kurzija'

Pišemo lahko tudi ``niz[i:j:k]``, s čimer vzamemo le vsak ``k``-ti znak:

.. doctest::

    >>> 'rekurzija'[1:8]
    'ekurzij'
    >>> 'rekurzija'[1:8:1]
    'ekurzij'
    >>> 'rekurzija'[1:8:2]
    'euzj'
    >>> 'rekurzija'[1:8:3]    
    'erj'
    >>> 'rekurzija'[::-1]
    'ajizruker'


Stavek ``print``
----------------

