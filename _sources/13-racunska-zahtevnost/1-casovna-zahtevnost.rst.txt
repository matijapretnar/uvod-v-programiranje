Časovna zahtevnost
==================

Kako bi lahko natančneje primerjali učinkovitost (običajno nas zanima čas, ki ga algoritem potrebuje, da izračuna odgovor) raznih algoritmov, ki smo jih srečali? Lahko bi izmerili čas, ki ga potrebujejo za izvedbo, vendar se to število spreminja od računalnika do računalnika. Tudi če bi se odločili za standardni računalnik, tako kot se odločimo za standardni kilogram ali meter, bi bilo za točne številke potrebno veliko truda, saj običajno želimo poznati učinkovitost algoritma pri različno velikih vhodnih podatkih, ocenili pa bi jih tudi zelo težko, saj bi morali natančno poznati, kako ta standardni računalnik deluje. Konec koncev pa v praksi tako natančnih številk sploh ne rabimo. Namesto tega se odločimo za pristop, v katerem lahko enostavno izračunamo grobe ocene, ki se v praksi izkažejo za dovolj dobre.

Zavoljo poenostavitve bomo privzeli dve predpostavki:

1. Zanimajo nas vrednosti le pri dovolj velikih številih, s čimer lahko zanemarimo manjša nihanja zaradi robnih pogojev.
2. Ne zanimajo nas konstantni faktorji, torej to, ali en algoritem vedno porabi dvakrat več časa od drugega.

O-notacija
----------

V ta namen bomo uporabili *O-notacijo*, s katero opišemo, s čim je v neskončnosti omejena rast funkcije. Ideja je sledeča.

Funkcija :math:`f(n) = n^3 + 3 n^2 + 3` je od nekod naprej omejena s funkcijo :math:`g(n) = 2 n^3 - 10`, čeprav je :math:`f(1) > g(1)` ali :math:`f(2) > g(2)`, saj bo vodilni člen pri velikih vrednostih :math:`n` prevladal nad ostalimi. Na primer, za vse :math:`n \ge 4` bo veljalo :math:`f(n) < g(n)`.

Kot smo dejali, nas konstantni faktorji ne zanimajo, zato lahko rečemo, da je rast funkcije :math:`f` omejena tudi s funkcijo :math:`k(n) = n^3`, saj bo za neko število :math:`b` od nekod naprej vedno veljalo :math:`f(n) \le b n^3`. Na primer, za vse :math:`n > 3000` bo veljalo :math:`f(n) \le 1.001 n^3`. Hitro lahko vidimo, da je rast kakršnegakoli polinoma :math:`p(n) = a_k n^k + \cdots + a_1 n + a_0` omejena z njegovo največjo potenco, torej funkcijo :math:`n \mapsto n^k`.

Vendar funkcija :math:`f` ni omejena s funkcijo oblike :math:`h(n) = a n^2`, saj jo sčasoma preseže, ne glede vrednost koeficienta :math:`a`. Podobno eksponentna funkcija ne more biti omejena z nobenim polinomom.

Za funkcijo :math:`f` definiramo množico

.. math::

    O(f) = \{ g \colon \mathbb{N} \to \mathbb{N} \colon \exists n_0, M . \forall n > n_0 . g(n) \le M \cdot f(n) \}

(:math:`O`-notacija je ponavadi podana za realne funkcije, mi pa se bomo omejili na enostavnejši primer naravnih funkcij).

Množica :math:`O(f)` vsebuje vse tiste funkcije :math:`g`, ki so od nekod naprej omejene z :math:`f`. Natančneje, obstajata števili :math:`n_0` in :math:`M`, da velja :math:`g(n) \le M \cdot f(n)` za vse :math:`n > n_0`. Na primer, za funkciji :math:`f(n) = n^3 + 3 n^2 + 3` in :math:`k(n) = n^3`, kot smo ju videli zgoraj, velja :math:`f \in O(k)`, saj lahko vzamemo :math:`n_0 = 3001` in :math:`M = 1.001`.

Dostikrat namesto :math:`f \in O(g)` malo bolj površno pišemo kar :math:`f(n) \in O(g(n))`. V našem primeru bi torej pisali kar :math:`n^3 + 3 n^2 + 3 \in O(n^3)`. Nekateri pišejo celo :math:`f(n) = O(g(n))`, vendar je tu treba paziti, saj ne gre za enakost. Velja namreč :math:`n^2 + 5 = O(n^2)` ter :math:`2 n^2 + n = O(n^2)`, vsekakor pa ne velja :math:`n^2 + 5 = 2 n^2 + n`.

Iz zgornje definicije lahko hitro izpeljemo:

.. math::

    f_1 \in O(g_1) \land f_2 \in O(g_2) \implies f_1 + f_2 \in O(g_1 + g_2)

kar običajno zapišemo kar kot

.. math::

    O(g_1) + O(g_2) = O(g_1 + g_2)

Podobno velja:

.. math::

    f_1 \in O(g_1) \land f_2 \in O(g_2) \implies f_1 \cdot f_2 \in O(g_1 \cdot g_2)

ali kar

.. math::

    O(g_1) \cdot O(g_2) = O(g_1 \cdot g_2)

ter

.. math::

    f \in O(g) \implies k \cdot f \in O(g)

ali kar

.. math::

    k \cdot O(g) = O(g)
