Iskanje
=======

Eden najosnovnejših problemov, ki ga rešujemo z računalniki, je iskanje določenega
podatka v veliki zbirki. Pri tem obravnavamo dve varianti:

1. Dano imamo zbirko elementov, nas pa zanima, ali iskani element v njej obstaja.
Na primer, zanima nas, ali se beseda *drabostljiv* pojavi v slovarju slovenskega
knjižnega jezika.

2. Dano imamo zbirko ključev in pripadajočih vrednosti, nas pa zanima, ali ima
iskani ključ v zbirki pripadajočo vrednost in kakšna je. Na primer, zanima nas
ne samo to, ali je beseda *drabostljiv* v slovarju, temveč tudi to, kakšno je
geslo, ki ji pripada.


Iskanje v neurejenem seznamu
----------------------------

Za začetek predpostavimo, da je naša zbirka predstavljena z neurejenim seznamom,
v katerem so našteti vsi elementi. Na primer:

.. code::

    sskj = ['miza', 'vesel', 'žaga', ..., 'razsvetljenstvo']

Če je seznam neurejen, obstaja bolj ali manj le en način, s katerim ugotovimo,
ali se element v seznamu pojavi: sprehodimo se čez vse elemente seznama od
prvega do zadnjega (lahko tudi od zadnjega do prvega) in vsakega primerjamo z
iskanim. Če najdemo enakega, je iskani element v seznamu. Če pa preiščemo vse
elemente in ne najdemo enakega, iskanega elementa v seznamu ni.

.. testcode::

    def poisci_v_neurejenem(seznam, iskani_element):
        '''Vrne True, kadar se iskani element pojavi v seznamu, in False, kadar se ne.'''
        for element in seznam:
            if element == iskani_element:
                return True
        return False


.. doctest::

    >>> poisci_v_neurejenem([1, 5, 2, 3], 4)
    False
    >>> poisci_v_neurejenem([1, 5, 2, 3], 3)
    True

Boljše rešitve od tega, da preiščemo vse elemente, žal ni. Če kakšen algoritem
ne bi pregledal vseh elementov, preden bi se odločil, da iskanega elementa ni
v seznamu, bi lahko vse elemente, ki si jih je ogledal, zamenjali z iskanim,
algoritem pa bi se še vedno odločil, da iskanega elementa v seznamu ni, saj bi
v drugo glede na pregledane elemente moral sprejeti iste odločitve kot prvič.

Z neurejenim seznamom parov lahko predstavimo tudi zbirko ključev in pripadajočih
vrednosti:

.. code::

    sskj = [('miza', 'lesen predmet za odlaganje krožnikov),
            ('vesel', 'tisti, ki izraža veselje'),
            ('žaga', 'orodje za žaganje'), ...,
            ('razsvetljenstvo', 'zgodovinsko obdobje, znano po žarnicah')]

Postopek za iskanje je podoben prejšnjemu, le da se tokrat vozimo čez pare in
ključe primerjamo z iskanim. Če najdemo ujemajoč ključ, vrnemo pripadajočo
vrednost, sicer pa vrnemo ``None``.

.. testcode::

    def poisci_vrednost_v_neurejenem(seznam, iskani_kljuc):
        '''Vrne pripadajočo vrednost ključa v seznamu. Ce je ni, vrne None.'''
        for kljuc, vrednost in seznam:
            if iskani_kljuc == kljuc:
                return vrednost
        return None

.. doctest::

    >>> poisci_vrednost_v_neurejenem([(7, 'a'), (4, 'r'), (8, 't')], 7)
    'a'
    >>> poisci_vrednost_v_neurejenem([(7, 'a'), (4, 'r'), (8, 't')], 5)
    >>> poisci_vrednost_v_neurejenem([(7, 'a'), (4, 'r'), (8, 't')], 'r')

Tudi v zadnjem klicu smo dobili rezultat ``None``, saj se ``'r'`` v seznamu
pojavi le kot vrednost, ne kot ključ.

Iskanje v urejenem seznamu
--------------------------

Če je seznam urejen, lahko vrednosti najdemo precej hitreje, saj približno vemo,
kje bi se iskani element moral pojaviti.

.. testcode::

    def poisci_v_urejenem(seznam, x, zac=0, kon=None):
        '''Vrne True, kadar se x pojavi v seznamu, in False, kadar se ne.'''
        if kon == None:
            kon = len(seznam)
        if zac == kon:
            return False

        sredina = (kon + zac) // 2

        if x == seznam[sredina]:
            return True

        elif x < seznam[sredina]:
            return poisci_v_urejenem(seznam, x, zac, sredina)

        elif x > seznam[sredina]:
            return poisci_v_urejenem(seznam, x, sredina + 1, kon)
