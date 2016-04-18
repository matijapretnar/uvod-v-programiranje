Časovna zahtevnost
==================

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
