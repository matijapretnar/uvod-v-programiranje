def prestej_samoglasnike_rek(niz):
    if niz == "":
        return 0
    preostanek_niza = niz[1:]
    samoglasniki_v_preostanku = prestej_samoglasnike_rek(preostanek_niza)
    if niz[0].lower() in "aeiou":
        return samoglasniki_v_preostanku + 1
    else:
        return samoglasniki_v_preostanku

def prestej_samoglasnike_for_z_indeksi(niz):
    stevec = 0
    for indeks in range(len(niz)):
        znak = niz[indeks]
        if znak.lower() in "aeiou":
            stevec = stevec + 1
    return stevec

def prestej_samoglasnike_for(niz):
    stevec = 0
    for znak in niz:
        if znak.lower() in "aeiou":
            stevec = stevec + 1
    return stevec

def filtriraj(niz, obdrzimo):
    filtrirani_niz = ''
    for znak in niz:
        if znak.lower() in obdrzimo.lower():
            filtrirani_niz += znak
        else:
            filtrirani_niz += '_'
    return filtrirani_niz

import string

def pretvori(niz, osnova):
    stevilo = 0
    cifre = string.digits + string.ascii_uppercase
    potenca = 0
    for znak in niz[::-1]:
        vrednost_cifre = cifre.index(znak)
        stevilo += vrednost_cifre * osnova ** potenca
        potenca += 1
    return stevilo

def pretvori(niz, osnova):
    stevilo = 0
    cifre = string.digits + string.ascii_uppercase
    for indeks in range(len(niz)):
        znak = niz[indeks]
        vrednost_cifre = cifre.index(znak)
        potenca = len(niz) - indeks - 1
        stevilo += vrednost_cifre * osnova ** potenca
    return stevilo

def izbrisi_podvojene(niz):
    pobrisani_niz = ''
    prejsnji_znak = ''
    prejsnji_znak_smo_videli_najvec_enkrat = True
    for znak in niz:
        if znak == prejsnji_znak:
            # prišli smo do istega znaka
            prejsnji_znak_smo_videli_najvec_enkrat = False
        else:
            # prisli smo do različnega znaka
            if prejsnji_znak_smo_videli_najvec_enkrat:
                pobrisani_niz += prejsnji_znak
            prejsnji_znak = znak
            prejsnji_znak_smo_videli_najvec_enkrat = True
    if prejsnji_znak_smo_videli_najvec_enkrat:
        pobrisani_niz += prejsnji_znak
    return pobrisani_niz