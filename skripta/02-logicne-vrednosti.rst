Logične vrednosti
=================

Poleg števil Python pozna tudi logični vrednosti ``True`` in ``False``, ki
označujeta resnico in neresnico. Logične vrednosti ponavadi dobimo kot rezultat
primerjav, kot so enakost ``==``, neenakost ``!=`` ali urejenostne relacije
``<``, ``>``, ``<=``, ``>=``, ter prek logičnih operacij ``and``, ``or`` in
``not``.

.. doctest::

    >>> 1 + 1 == 3
    False
    >>> 3 != 2
    True
    >>> True and False
    False
    >>> not (5 == 10)
    True
    >>> 3 < 5 or 10 > 20
    True


Pogojni stavek
--------------

Logične vrednosti uporabimo v *pogojnih stavkih* (oziroma ``if``-stavkih) oblike

.. code::

    if pogoj:
        stavki_ki_jih_izvedemo
        ko_pogoj_drzi
    else:
        stavki_ki_jih_izvedemo
        ko_pogoj_ne_drzi

Ključnima besedama ``if``/``else`` in pripadajočim stavkom pravimo tudi *veje
pogojnega stavka*. Stavke v obeh vejah moramo zamakniti za štiri presledke,
da se jasno vidi, kam spadajo.

Na primer, če izvedemo program

.. testcode::

    x = 5
    if x < 10:
        x *= 2
    else:
        x = 3 * x
        x -= 1
    x += 7

se bo izvedla veja ``if``, zato bo ``x`` na koncu enak 17. V primeru, da bi bila
začetna vrednost ``x = 12``, pa bi se izvedla veja ``else`` in vrednost ``x`` bi
na koncu bila 42.

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

Izračunajmo število točk zmagovalnega skoka `Petra Prevca na letalnici v
Vikersundu`__. Peter je skočil 249 metrov, vendar padel, zaradi česar je dobil
bolj slabe sodniške ocene: 15,0, 12,5, 14,0, 13,5 in 11,0. Koliko točk je dobil
za skok? Kodo napišimo tako, da bo delovala tudi v primeru, ko za K-točko,
dolžino skoka, ocene sodnikov in izravnavo vnesemo druga števila. Kot vidimo,
potrebujemo pogojni stavek, v katerem ustrezno izračunamo točke za dolžino
skoka.

__ http://medias3.fis-ski.com/pdf/2016/JP/3815/2016JP3815RL.pdf

.. testcode::

    k_tocka = 200
    dolzina = 249.0
    slog_a = 15
    slog_b = 12.5
    slog_c = 14
    slog_d = 13.5
    slog_e = 11
    izravnava = 6.4

    # če je K-točka vsaj 170 metrov, gre za letalnico
    if k_tocka >= 170:
        osnovne_tocke = 120
        vrednost_metra = 1.2
    else:
        osnovne_tocke = 60
        vrednost_metra = 1.8
    tocke_dolzina = 120 + vrednost_metra * (dolzina - k_tocka)

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
    225.20000000000002

Skok je bil v resnici vreden natanko 225,2 točk. Vse dodatne decimalke pa so
posledica zaokrožitvenih napak. Računalnik namreč ne računa s pravimi realnimi
števili, temveč z njihovimi približki, ki jim pravimo *števila s plavajočo
vejico*.

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


Manjkajoča veja ``else``
------------------------

Če želimo, lahko vejo ``else`` tudi izpustimo (tako v običajnem kot v
razširjenem pogojnem stavku). V tem primeru se ob neizpolnjevanju pogoja ne
zgodi nič. Na ta način bi izračun osnovnih točk lahko pisali tudi kot:

.. doctest::

    osnovne_tocke = 60
    if k_tocka >= 170:
        osnovne_tocke = 120

Torej, ``osnovne_tocke`` najprej nastavimo na 60, v primeru da gre za letalnico,
pa jih popravimo na 120. Vrstni red izvajanja je seveda pomemben. Če bi pisali

.. doctest::

    if k_tocka >= 170:
        osnovne_tocke = 120
    osnovne_tocke = 60

bi osnovne točke vedno nastavili na 60.

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
