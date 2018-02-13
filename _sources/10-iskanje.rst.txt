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
        '''Vrne True, če se iskani element pojavi v seznamu, in False, če se ne.'''
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
            if kljuc == iskani_kljuc:
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

Če je seznam urejen, lahko iskani element poiščemo bistveno hitreje z bisekcijo.
V seznamu si pogledamo element na sredini. Če je slučajno enak iskanemu elementu,
smo končali, sicer pa je bodisi večji bodisi manjši. Če je sredinski element
večji od iskanega, potem vemo, da se iskani element ne more pojaviti v desni
polovici, saj so vsi tamkajšnji elementi zaradi urejenosti večji od sredinskega.
Tako lahko iskanje zožimo le na levo polovico seznama. Če je sredinski element
manjši od iskanega, pa iskanje zožimo na desno polovico seznama. V obeh primerih
iskanje nadaljujemo na polovico manjšem seznamu, kjer uporabimo enak postopek.
To nadaljujemo dokler iskanja ne zožimo na seznam dolžine 1. V tem primeru
le pogledamo, če je edini element enak iskanemu. Če je, smo iskani element našli,
če ni, pa ga v seznamu ni bilo.

Bisekcijo lahko implementiramo na več načinov. Prvi je, da v spremenljivkah
``zacetek`` in ``konec`` hranimo začetni in končni indeks podseznama, v katerem
iščemo element. V skladu s Pythonovimi standardi, v spremenljivki ``konec`` ne
bomo hranili zadnjega indeksa v podseznamu, temveč naslednji indeks. Na začetku
bomo element iskali v celotnem seznamu, zato bo ``zacetek`` enak 0, ``konec``
pa dolžini seznama. Odvisno od tega, kakšen je sredinski element v primerjavi z
iskanim, bomo spremenljivki ``zacetek`` in ``konec`` ustrezno popravljali. Ko se
indeksa izenačita, postopek končamo, saj je tedaj podseznam prazen.

.. testcode::

    def poisci_v_urejenem_z_zanko(seznam, iskani_element):
        '''Vrne True, če se iskani element pojavi v urejenem seznamu, in False, če se ne.'''
        zacetek = 0
        konec = len(seznam)

        while zacetek < konec:
            sredina = (zacetek + konec) // 2
            if seznam[sredina] == iskani_element:
                return True
            elif seznam[sredina] < iskani_element:
                zacetek = sredina + 1
            elif seznam[sredina] > iskani_element:
                konec = sredina

        return False

.. doctest::

    >>> poisci_v_urejenem_z_zanko([1, 2, 3, 5], 4)
    False
    >>> poisci_v_urejenem_z_zanko([1, 2, 3, 5], 3)
    True

Seveda funkcija ne bo delala pravilno, če ji ne bomo podali urejenega seznama:

.. doctest::

    >>> poisci_v_urejenem_z_zanko([3, 3, 3, 1, 5, 5, 5], 3)
    False


Enak postopek zapišemo tudi rekurzivno, vendar moramo biti pri tem malo bolj
previdni. Načeloma lahko iskanje v podseznamu naredimo tako, da s pomočjo rezin
ustvarili manjši seznam in iščemo v njem:

.. testcode::

    def poisci_v_urejenem_z_rezinami(seznam, iskani_element):
        '''Vrne True, če se iskani element pojavi v urejenem seznamu, in False, če se ne.'''
        if len(seznam) == 0:
            return False
        else:
            sredina = len(seznam) // 2
            if seznam[sredina] == iskani_element:
                return True
            elif seznam[sredina] < iskani_element:
                return poisci_v_urejenem_z_rezinami(seznam[sredina + 1:], iskani_element)
            elif seznam[sredina] > iskani_element:
                return poisci_v_urejenem_z_rezinami(seznam[:sredina], iskani_element)

.. doctest::

    >>> poisci_v_urejenem_z_rezinami([1, 2, 3, 5], 4)
    False
    >>> poisci_v_urejenem_z_rezinami([1, 2, 3, 5], 3)
    True

Taka funkcija sicer deluje pravilno, vendar opravlja nepotrebno delo, saj
ob vsakem rekurzivnem klicu naredi novo rezino (bodisi ``seznam[sredina + 1:]``
bodisi ``seznam[:sredina]``), kar zahteva, da vse ustrezne elemente presname
na novo mesto. Bolje je, da tako kot pri rešitvi z zankami ves čas delamo z
istim seznamom, vendar si zapomnimo, med katerima dvema indeksoma iščemo element.

.. testcode::

    def poisci_v_urejenem_med_indeksoma(seznam, iskani_element, zacetek, konec):
        '''Vrne True, če se iskani element pojavi v urejenem seznamu na mestu i,
        kjer je zacetek <= i < konec, in False, če se ne.'''
        if zacetek == konec:
            return False
        else:
            sredina = (zacetek + konec) // 2
            if seznam[sredina] == iskani_element:
                return True
            elif seznam[sredina] < iskani_element:
                return poisci_v_urejenem_med_indeksoma(seznam, iskani_element, sredina + 1, konec)
            elif seznam[sredina] > iskani_element:
                return poisci_v_urejenem_med_indeksoma(seznam, iskani_element, zacetek, sredina)

.. doctest::

    >>> poisci_v_urejenem_med_indeksoma([1, 2, 3, 5], 4, 0, 3)
    False
    >>> poisci_v_urejenem_med_indeksoma([1, 2, 3, 5], 3, 0, 3)
    True
    >>> poisci_v_urejenem_med_indeksoma([1, 2, 3, 5], 3, 0, 2)
    False

Ta rešitev je veliko bolj učinkovita, saj ne ustvarja novih elementov, je pa malo
moteče, ker moramo vsakič podajati meje. Če tega ne želimo, lahko uporabimo bodisi
pomožno funkcijo:

.. testcode::

    def poisci_v_urejenem(seznam, iskani_element):
        '''Vrne True, če se iskani element pojavi v urejenem seznamu, in False, če se ne.'''
        return poisci_v_urejenem_med_indeksoma(seznam, iskani_element, 0, len(seznam))

bodisi argumentoma ``zacetek`` in ``konec`` damo privzeti vrednosti:

.. testcode::

    def poisci_v_urejenem_med_indeksoma(seznam, iskani_element, zacetek=0, konec=None):
        '''Vrne True, če se iskani element pojavi v urejenem seznamu na mestu i,
        kjer je zacetek <= i < konec, in False, če se ne.'''
        if konec is None:
            konec = len(seznam)

        if zacetek == konec:
            return False
        else:
            sredina = (zacetek + konec) // 2
            if seznam[sredina] == iskani_element:
                return True
            elif seznam[sredina] < iskani_element:
                return poisci_v_urejenem_med_indeksoma(seznam, iskani_element, sredina + 1, konec)
            elif seznam[sredina] > iskani_element:
                return poisci_v_urejenem_med_indeksoma(seznam, iskani_element, zacetek, sredina)

.. doctest::

    >>> poisci_v_urejenem_med_indeksoma([1, 2, 3, 5], 3, 0, 3)
    True
    >>> poisci_v_urejenem_med_indeksoma([1, 2, 3, 5], 3)
    True
    >>> poisci_v_urejenem_med_indeksoma([1, 2, 3, 5], 3, 0, 2)
    False

Kot vidimo, smo privzeto vrednost argumenta ``zacetek`` nastavili na 0,
privzete vrednosti argumenta ``konec`` pa nismo nastavili na dolžino seznama.
Razlog je v tem, da vrednost privzetega argumenta lahko nastavimo le enkrat:
takrat, ko funkcijo definiramo. Ker pa hočemo funkcijo uporabiti na seznamih
različnih dolžin, nobena privzeta vrednost ne bo prava. Običajna rešitev je,
da argumentom, za katere lahko privzete vrednosti izračunamo šele ob klicu
funkcije, nastavimo privzeto vrednost ``None``. Nato pa ob klicu funkcije v
primerih, ko se je uporabila ta privzeta vrednost, vrednost argumenta
ustrezno popravimo. V našem primeru smo takrat, ko je bila vrednost spremenljivke
``konec`` enaka ``None``, njeno vrednost nastavili na dolžino danega seznama.
V primeru, ko smo ob klicu funkcije vrednost argumenta ``konec`` podali (torej
ob rekurzivnih klicih), pa bo ta vrednost različna od ``None``, zato se ne
bo zgodilo nič.
