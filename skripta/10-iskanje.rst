Iskanje
=======

Iskanje v neurejenem seznamu
----------------------------


.. testcode::

    def poisci_v_neurejenem(seznam, x):
        '''Vrne True, kadar se x pojavi v seznamu, in False, kadar se ne.'''
        for y in seznam:
            if x == y:
                return True
        return False
    

.. testcode::

    def poisci_vrednost_v_neurejenem(seznam, iskani_kljuc):
        '''Vrne pripadajočo vrednost ključa v seznamu. Ce je ni, vrne None.'''
        for kljuc, vrednost in seznam:
            if iskani_kljuc == kljuc:
                return vrednost
        return None


Iskanje v urejenem seznamu
--------------------------


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
