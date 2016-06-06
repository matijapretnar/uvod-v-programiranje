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

O-notacija
----------

.. math::

    f \in O(g) \iff \exists n_0, M . \forall n > n_0 . |f(n)| \le M \cdot |g(n)|

.. math::

    f \in O(g) \iff f(n) \in O(g(n)) \iff f(n) = O(g(n))


Pravila za računanje z O-notacijo
---------------------------------

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

časovna zahtevnost: iskanje v neurejenem, iskanje v urejenem, je_podseznam
