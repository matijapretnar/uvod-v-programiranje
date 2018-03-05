
Dokumentacijski niz*
--------------------

Pred telesom funkcije dostikrat lahko zapišemo tudi  *dokumentacijski niz* oziroma *docstring*. Ta niz ponavadi zapišemo med trojne enojne navednice, v njem pa na kratko opišemo, kaj funkcija počne. Ta vrstica ni obvezna, je pa koristna, saj lahko uporabnik, ki ne ve, kaj funkcija počne, to pogleda s pomočjo funkcije ``help``.

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



Primer: smučarski skoki
-----------------------

Za primer iz rezultatov smučarskega skoka, torej dolžine in ocen sodnikov,
izračunajmo skupne točke. Vsaka skakalnica ima določeno K-točko, ki določa
velikost skakalnice. Skok za dolžino v osnovi dobi 60 točk (za letalnice 120),
nato pa vsak meter nad ali pod K-točko prinese oziroma odnese 1,8 točke (za
letalnice 1,2).

Točke za slog pa dobimo tako, da seštejemo vse ocene sodnikov razen najnižje in
najvišje. To najenostavneje izračunamo tako, da seštejemo vse ocene, nato pa
odštejemo najnižjo in najvišjo, ki ju dobimo s pomočjo vgrajenih funkcij ``min``
in ``max``. Skupno oceno dobimo tako, da seštejemo točke za dolžino, točke za
slog in točke za izravnavo vetra in zaletišča.

Izračunajmo število točk zmagovalnega skoka `Petra Prevca na skakalnici v
Sapporu`__. Peter je skočil 138 metrov ter dobil sodniške ocene:
18,5, 18,5, 19,0, 19,0 in 19,0. Koliko točk je dobil za skok?
Kodo napišimo tako, da bo delovala tudi v primeru, ko za K-točko,
dolžino skoka, ocene sodnikov in izravnavo vnesemo druga števila. Kot vidimo,
potrebujemo pogojni stavek, v katerem ustrezno izračunamo točke za dolžino
skoka.

__ http://medias2.fis-ski.com/pdf/2017/JP/3906/2017JP3906RL.pdf

.. testcode::

    k_tocka = 123
    dolzina = 138.0
    slog_a = 18.5
    slog_b = 18.5
    slog_c = 19
    slog_d = 19
    slog_e = 19
    izravnava = -16.6

    # če je K-točka vsaj 170 metrov, gre za letalnico
    if k_tocka >= 170:
        osnovne_tocke = 120
        vrednost_metra = 1.2
    else:
        osnovne_tocke = 60
        vrednost_metra = 1.8
    tocke_dolzina = osnovne_tocke + vrednost_metra * (dolzina - k_tocka)

    min_slog = min(slog_a, slog_b, slog_c, slog_d, slog_e)
    max_slog = max(slog_a, slog_b, slog_c, slog_d, slog_e)
    tocke_slog = (slog_a + slog_b + slog_c + slog_d + slog_e) - min_slog - max_slog

    skupne_tocke = tocke_dolzina + tocke_slog + izravnava

Poleg že znanih ukazov v zgornji kodi vidimo tudi *komentar*. Ko Python v kodi
vidi lojtro ``#``, preostanek vrstice ignorira. Namen komentarjev je, da po
človeško razložimo tiste dele kode, ki niso očitni. Ker so programi v Pythonu
precej razumljivi (sploh, ker uporabljamo opisna imena spremenljivk), ponavadi
ni treba pisati veliko komentarjev.

Poglejmo, koliko točk je bil vreden skok:

.. doctest::

    >>> skupne_tocke
    126.9

Razširjeni pogojni stavek
-------------------------

V resnici tudi zgornja formula ni čisto natančna, saj obstajajo tudi male skakalnice,
na katerih je vrednost metra enaka 2. Tako bi morali točke za dolžino izračunati kot:


.. doctest::

    if k_tocka >= 170:
        osnovne_tocke = 120
        vrednost_metra = 1.2
    else:
        if k_tocka >= 100:
            osnovne_tocke = 60
            vrednost_metra = 1.8
        else:
            osnovne_tocke = 60
            vrednost_metra = 2

Zgornji pogojni stavek je malo nerodno zapisan. Ker se nam bo dostikrat zgodilo,
da se ne bomo odločali le med dvema primeroma, temveč med večimi, nam Python omogoča
splošnejše pogojne stavke oblike:

.. code::

    if pogoj1:
        stavki_ki_jih_izvedemo
        ko_pogoj1_drzi
    elif pogoj2:
        stavki_ki_jih_izvedemo
        ko_pogoj1_ne_drzi
        ampak_drzi_pogoj2
    elif pogoj3:
        stavki_ki_jih_izvedemo
        ko_tudi_pogoj2_ne_drzi
        ampak_drzi_pogoj3
    else:
        stavki_ki_jih_izvedemo
        ko_noben_od_pogojev_ne_drzi

Beseda ``elif`` je okrajšava za ``else``-``if``. Točke za razdaljo bi tako lepše zapisali kot:

.. doctest::

    if k_tocka >= 170:
        osnovne_tocke = 120
        vrednost_metra = 1.2
    elif k_tocka >= 100:
        osnovne_tocke = 60
        vrednost_metra = 1.8
    else:
        osnovne_tocke = 60
        vrednost_metra = 2

ali pa kot:

.. doctest::

    if k_tocka >= 170:
        osnovne_tocke = 120
    else:
        osnovne_tocke = 60

    if k_tocka >= 170:
        vrednost_metra = 1.2
    elif k_tocka >= 100:
        vrednost_metra = 1.8
    else:
        vrednost_metra = 2

Kot lahko vidite na `Wikipediji`__, je ocenjevanje še bolj zapleteno, vendar
pogojnemu stavku ne bomo dodajali še novih in novih vej, temveč bomo počakali na
to, da spoznamo malo boljšo rešitev.

__ https://en.wikipedia.org/wiki/Construction_point


Izrazi & stavki
---------------

V Pythonovih programih ločimo med *izrazi* in *stavki*. Izrazi so vse, kar
sestavimo iz funkcij in operacij ter uporabljamo kot argumente funkcij, desne
strani prireditvenih izrazov ali pogoje v pogojnih stavkih. Stavki pa so osnovni
gradniki Pythonovih programov in jih pišemo enega pod drugim. Zaenkrat smo
videli tri vrste stavkov: prva so bili prireditveni stavki, drugi pogojni stavki
(ki so potem spet sestavljeni iz gnezdenih stavkov), tretja in najmanj opazna pa
so bili izrazi. Običajne izraze lahko prav tako pišemo v programe, vendar ne bodo
imeli posebnega učinka. Če napišemo

.. testcode::

    x = 10
    10 + 10
    y = 20

se bo vsota ``10 + 10`` res izračunala, vendar se ne bo nikamor shranila in
Python bo na njo hitro pozabil. Kmalu pa bomo srečali tudi izraze, ki bodo imeli
vpliv na nadaljnje izvajanje programov.

Pogojni izraz
-------------

O razliki med izrazi in stavki govorimo o tem, ker Python poleg pogojnih stavkov
podpira tudi pogojne izraze, s katerimi nekatere stvari napišemo malo elegantneje.
Na primer, zgornjo določitev osnovnih točk bi lahko pisali kot:

.. testcode::

    osnovne_tocke = 120 if k_tocka >= 170 else 60

Če bi na isti način želeli uporabiti pogojni stavek

.. code::

    osnovne tocke = if k_tocka >= 170:
        120
    else:
        60

bi dobili sintaktično napako, saj smo na mestu izraza uporabili stavek. V
pogojnih izrazih moramo vedno napisati obe možnosti, prav tako pa ne moremo
uporabiti ``elif``-a, zato spremenljivke ``vrednost_metra`` z njimi ne bi mogli
nastaviti. No, načeloma bi jo lahko z

.. testcode::

    vrednost_metra = 1.2 if k_tocka >= 170 else 1.8 if k_tocka >= 100 else 2

samo to je preveč natlačeno, da bi bilo berljivo. Pogojni stavki so torej precej
omejeni, ampak vseeno jih omenjamo, ker znajo včasih kakšno stvar narediti
preglednejšo.



Pogojni izraz
-------------

ali s pogojnim izrazom kot:

.. testcode::

    def fakulteta(n):
        '''Vrne fakulteto naravnega števila n.'''
        return 1 if n == 0 else n * fakulteta(n - 1)

ali s pogojnim izrazom kot

.. testcode::

    def gcd(m, n):
        '''Vrne največji skupni delitelj števil m in n.'''
        return m if n == 0 else gcd(n, m % n)



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
        ustavi_program
        javi_napako

ampak ker je to pogosto koristno, so v ta namen uvedli ``assert``.
