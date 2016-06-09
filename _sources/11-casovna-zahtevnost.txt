Časovna zahtevnost
==================

Kako bi lahko natančneje primerjali učinkovitost (običajno nas zanima čas, ki ga
algoritem potrebuje, da izračuna odgovor) raznih algoritmov, ki smo jih srečali?
Lahko bi izmerili čas, ki ga potrebujejo za izvedbo, vendar se to število
spreminja od računalnika do računalnika. Tudi če bi se odločili za standardni
računalnik, tako kot se odločimo za standardni kilogram ali meter, bi bilo za
točne številke potrebno veliko truda, saj običajno želimo poznati učinkovitost
algoritma pri različno velikih vhodnih podatkih, ocenili pa bi jih tudi zelo
težko, saj bi morali natančno poznati, kako ta standardni računalnik deluje.
Konec koncev pa v praksi tako natančnih številk sploh ne rabimo. Namesto tega se
odločimo za pristop, v katerem lahko enostavno izračunamo grobe ocene, ki se v
praksi izkažejo za dovolj dobre.

Zavoljo poenostavitve bomo privzeli dve predpostavki:

1. Zanimajo nas vrednosti le pri dovolj velikih številih, s čimer lahko zanemarimo
manjša nihanja zaradi robnih pogojev.
2. Ne zanimajo nas konstantni faktorji, torej to, ali en algoritem vedno porabi 
dvakrat več časa od drugega.

O-notacija (razlaga še manjka)
------------------------------

V ta namen bomo uporabili *O-notacijo*, s katero združujemo funkcije, ki se
v neskončnosti obnašajo podobno. Za funkciji :math:`f` in :math:`g` definiramo

.. math::

    f \in O(g) \iff \exists n_0, M . \forall n > n_0 . |f(n)| \le M \cdot |g(n)|

kar preberemo kot “:math:`f` pripada razredu :math:`O(g)`”. V našem primeru nas
bodo zanimale le pozitivne funkcije (ker algoritem za izvajanje ne bo potreboval
negativne količine časa), zato definicijo takoj poenostavimo na:

.. math::

    f \in O(g) \iff \exists n_0, M . \forall n > n_0 . f(n) \le M \cdot g(n)

Ideja je sledeča: :math:`f \in O(g)` velja natanko takrat, kadar je funkcija :math:`f`
od nekod naprej (za vsa števila :math:`n` od nekega :math:`n_0` naprej) omejena
s funkcijo :math:`g`.

.. math::

    f \in O(g) \iff f(n) \in O(g(n)) \iff f(n) = O(g(n))


.. math::

    f_1 \in O(g_1) \land f_2 \in O(g_2) \implies f_1 + f_2 \in O(g_1 + g_2)

ali kar

.. math::

    O(g_1) + O(g_2) = O(g_1 + g_2)

Če sta $g_1$ in $g_2$ pozitivni funkciji.

.. math::

    f_1 \in O(g_1) \land f_2 \in O(g_2) \implies f_1 \cdot f_2 \in O(g_1 \cdot g_2)

ali kar

.. math::

    O(g_1) \cdot O(g_2) = O(g_1 \cdot g_2)

.. math::

    f \in O(g) \implies k \cdot f \in O(g)

ali kar

.. math::

    k \cdot O(g) = O(g)

Časovne zahtevnosti do sedaj videnih algoritmov (vsebina še manjka)
-------------------------------------------------------------------
