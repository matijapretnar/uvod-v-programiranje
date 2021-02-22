# Kako deluje Python

## Uporaba razhroščevalnika

.small[![](slike/hrosc.jpg)]

## Klicni sklad

## Knjižnica `sys`

## Spremenljivke, imena, objekti

## Predstavitev v pomnilniku

## Računska zahtevnost

**Časovna** zahtevnost

Koliko **časa v odvisnosti od vhodnih podatkov** potrebuje algoritem za izračun rezultata.

**Prostorska** zahtevnost

Koliko **(dodatnega) prostora** v odvisnosti od vhodnih podatkov potrebuje algoritem za izračun rezultata.

Mi se bomo povečini ukvarjali s **časovno zahtevnostjo**.

Kako bi lahko natančneje primerjali učinkovitost (običajno nas zanima čas, ki ga algoritem potrebuje, da izračuna odgovor) raznih algoritmov, ki smo jih srečali? Lahko bi izmerili čas, ki ga potrebujejo za izvedbo, vendar se to število spreminja od računalnika do računalnika. Tudi če bi se odločili za standardni računalnik, tako kot se odločimo za standardni kilogram ali meter, bi bilo za točne številke potrebno veliko truda, saj običajno želimo poznati učinkovitost algoritma pri različno velikih vhodnih podatkih, ocenili pa bi jih tudi zelo težko, saj bi morali natančno poznati, kako ta standardni računalnik deluje. Konec koncev pa v praksi tako natančnih številk sploh ne rabimo. Namesto tega se odločimo za pristop, v katerem lahko enostavno izračunamo grobe ocene, ki se v praksi izkažejo za dovolj dobre.

Zavoljo poenostavitve bomo privzeli dve predpostavki:

1. Zanimajo nas vrednosti le pri dovolj velikih številih, s čimer lahko zanemarimo manjša nihanja zaradi robnih pogojev.
2. Ne zanimajo nas konstantni faktorji, torej to, ali en algoritem vedno porabi dvakrat več časa od drugega.

Kako **določiti** časovno zahtevnost?

- Z merjenjem porabljenega časa

- rezultati so **odvisni od računalnika**

- pri meritvah prihaja do **napak**

- program moramo **dejansko izvesti**

- Z natančno matematično analizo

- natančno moramo **poznati model** računanja

- analiza je **zahtevna**

- tako natančnih rezultatov **ne rabimo**

`timeit` in `matplotlib`

## O-notacija

V ta namen bomo uporabili _O-notacijo_, s katero opišemo, s čim je v neskončnosti omejena rast funkcije. Ideja je sledeča.

Funkcija $f(n) = n^3 + 3 n^2 + 3$ je od nekod naprej omejena s funkcijo $g(n) = 2 n^3 - 10$, čeprav je $f(1) > g(1)$ ali $f(2) > g(2)$, saj bo vodilni člen pri velikih vrednostih $n$ prevladal nad ostalimi. Na primer, za vse $n \ge 4$ bo veljalo $f(n) < g(n)$.

Kot smo dejali, nas konstantni faktorji ne zanimajo, zato lahko rečemo, da je rast funkcije $f$ omejena tudi s funkcijo $k(n) = n^3$, saj bo za neko število $b$ od nekod naprej vedno veljalo $f(n) \le b n^3$. Na primer, za vse $n > 3000$ bo veljalo $f(n) \le 1.001 n^3$. Hitro lahko vidimo, da je rast kakršnegakoli polinoma $p(n) = a_k n^k + \cdots + a_1 n + a_0$ omejena z njegovo največjo potenco, torej funkcijo $n \mapsto n^k$.

Vendar funkcija $f$ ni omejena s funkcijo oblike $h(n) = a n^2$, saj jo sčasoma preseže, ne glede vrednost koeficienta $a$. Podobno eksponentna funkcija ne more biti omejena z nobenim polinomom.

Za funkcijo $f$ definiramo množico

$$O(f) = { g \colon \mathbb{N} \to \mathbb{N} \colon \exists n_0, M . \forall n > n_0 . g(n) \le M \cdot f(n) }$$

($O$-notacija je ponavadi podana za realne funkcije, mi pa se bomo omejili na enostavnejši primer naravnih funkcij).

Množica $O(f)$ vsebuje vse tiste funkcije $g$, ki so od nekod naprej omejene z $f$. Natančneje, obstajata števili $n_0$ in $M$, da velja $g(n) \le M \cdot f(n)$ za vse $n > n_0$. Na primer, za funkciji $f(n) = n^3 + 3 n^2 + 3$ in $k(n) = n^3$, kot smo ju videli zgoraj, velja $f \in O(k)$, saj lahko vzamemo $n_0 = 3001$ in $M = 1.001$.

Dostikrat namesto $f \in O(g)$ malo bolj površno pišemo kar $f(n) \in O(g(n))$. V našem primeru bi torej pisali kar $n^3 + 3 n^2 + 3 \in O(n^3)$. Nekateri pišejo celo $f(n) = O(g(n))$, vendar je tu treba paziti, saj ne gre za enakost. Velja namreč $n^2 + 5 = O(n^2)$ ter $2 n^2 + n = O(n^2)$, vsekakor pa ne velja $n^2 + 5 = 2 n^2 + n$.

Iz zgornje definicije lahko hitro izpeljemo:

$$f_1 \in O(g_1) \land f_2 \in O(g_2) \implies f_1 + f_2 \in O(g_1 + g_2)$$

kar običajno zapišemo kar kot

$$O(g_1) + O(g_2) = O(g_1 + g_2)$$

Podobno velja:

$$f_1 \in O(g_1) \land f_2 \in O(g_2) \implies f_1 \cdot f_2 \in O(g_1 \cdot g_2)$$

ali kar

$$O(g_1) \cdot O(g_2) = O(g_1 \cdot g_2)$$

ter

$$f \in O(g) \implies k \cdot f \in O(g)$$

ali kar

$$k \cdot O(g) = O(g)$$

Analizo poenostavimo z **notacijo velikega O**

$$f \in O(g) \iff \exists \color{purple}{M}, \color{red}{x_0}. \forall x > \color{red}{x_0}. |f(x)| \leq \color{purple}{M} \cdot |\color{blue}{g}(x)|$$

.center[![](slike/O-graf.png)]

Rast funkcije $f$ je **omejena** s funkcijo $g$

Analizo poenostavimo z **notacijo velikega O**

$$f \in O(g) \iff \exists \color{purple}{M}, \color{red}{x_0}. \forall x > \color{red}{x_0}. |f(x)| \leq \color{purple}{M} \cdot |\color{blue}{g}(x)|$$

.center[![](slike/O-graf.png)]

Rast funkcije $f$ je **omejena** s funkcijo $g$

**Lastnosti** notacije velikega O

$$f \in O(g), a \in \mathbb{R} \implies a \cdot f \in O(g)$$

$$f_1 \in O(g_1), f_2 \in O(g_2) \implies f_1 + f_2 \in O(|g_1| + |g_2|)$$

$$f_1 \in O(g_1), f_2 \in O(g_2) \implies f_1 \cdot f_2 \in O(g_1 \cdot g_2)$$

Pri zapisu smo dostikrat **površni**

$$n \mapsto n^2 + 3 n \in O(n \mapsto n^2)$$ $$n^2 + 3 n \in O(n^2)$$ $$n^2 + 3 n = O(n^2)$$

Površni smo tudi pri **lastnostih**

$$a \cdot O(g) = O(g)$$ $$O(g_1) + O(g_2) = O(g_1 + g_2)$$ $$O(g_1) \cdot O(g_2) = O(g_1 \cdot g_2)$$

Katere trditve so veljavne?

| :----------------------------------: | :: $ 3 n^2 - 1000 n \in O(n^2) $ | .green.spoiler[**DA**] $ 1000 n^2 + 0.0001 n^3 \in O(n^2) $ | .red.spoiler[**NE**] $ 1000 n^2 + 0.0001 n^3 \in O(n^3) $ | .green.spoiler[**DA**] $ 1000 n^2 + 0.0001 n^3 \in O(n^4) $ | .green.spoiler[**DA**] $ n^{1000} + 2^n \in O(n^{1000}) $ | .red.spoiler[**NE**] $ n^{1000} + 2^n \in O(2^n) $ | .green.spoiler[**DA**]

**Kako izračunamo** časovno zahtevnost?

1. Pri **zaporednih** programih časovne zahtevnosti **seštejemo**

2. Pri **vejah** vzamemo **največjo** časovno zahtevnost

3. Pri **zankah** časovno zahtevnost **pomnožimo** s številom obhodov

## Časovna zahtevnost vgrajenih operacij

`sez[i]` `sez[i] = x`

$$O(1)$$

`len(sez)`

$$O(1)$$

`sez.append(x)`

$$O(1)$$

`sez.insert(0, x)`

$$O(n)$$

Izračun najmanjšega elementa v seznamu

$$O(n)$$

Izračun najmanjšega elementa v urejenem seznamu

$$O(1)$$

`min(sez)`

$$O(n)$$

`min(urejen_sez)`

$$O(n)$$

Iskanje elementa v neurejenem seznamu

$$O(n)$$

Iskanje elementa v urejenem seznamu

$$O(\log n)$$

`x in sez`

$$O(n)$$

`x in urejen_sez`

$$O(n)$$

`k in slovar` `x in mnozica`

$$O(1)$$

`slovar[k] = v` `mnozica.add(x)`

$$O(1)$$


## Iskanje z bisekcijo

Eden najosnovnejših problemov, ki ga rešujemo z računalniki, je iskanje določenega podatka v veliki zbirki. Pri tem obravnavamo dve varianti:

1. Dano imamo zbirko elementov, nas pa zanima, ali iskani element v njej obstaja. Na primer, zanima nas, ali se beseda _drabostljiv_ pojavi v slovarju slovenskega knjižnega jezika.
2. Dano imamo zbirko ključev in pripadajočih vrednosti, nas pa zanima, ali ima iskani ključ v zbirki pripadajočo vrednost in kakšna je. Na primer, zanima nas ne samo to, ali je beseda _drabostljiv_ v slovarju, temveč tudi to, kakšno je geslo, ki ji pripada.

Za začetek predpostavimo, da je naša zbirka predstavljena z neurejenim seznamom, v katerem so našteti vsi elementi. Na primer:

```
sskj = ['miza', 'vesel', 'žaga', ..., 'razsvetljenstvo']
```

Če je seznam neurejen, obstaja bolj ali manj le en način, s katerim ugotovimo, ali se element v seznamu pojavi: sprehodimo se čez vse elemente seznama od prvega do zadnjega (lahko tudi od zadnjega do prvega) in vsakega primerjamo z iskanim. Če najdemo enakega, je iskani element v seznamu. Če pa preiščemo vse elemente in ne najdemo enakega, iskanega elementa v seznamu ni.

```
def poisci_v_neurejenem(seznam, iskani_element):

:   """Vrne True, če se iskani element pojavi v seznamu, in False, če
    se ne.""" for element in seznam: if element == iskani_element:
    return True return False
```

```
```
```{code-cell}
poisci_v_neurejenem([1, 5, 2, 3], 4) False
>>>```
```{code-cell}
poisci_v_neurejenem([1, 5, 2, 3], 3) True
```

Boljše rešitve od tega, da preiščemo vse elemente, žal ni. Če kakšen algoritem ne bi pregledal vseh elementov, preden bi se odločil, da iskanega elementa ni v seznamu, bi lahko vse elemente, ki si jih je ogledal, zamenjali z iskanim, algoritem pa bi se še vedno odločil, da iskanega elementa v seznamu ni, saj bi v drugo glede na pregledane elemente moral sprejeti iste odločitve kot prvič.

Z neurejenim seznamom parov lahko predstavimo tudi zbirko ključev in pripadajočih vrednosti:

```
sskj = [('miza', 'lesen predmet za odlaganje krožnikov),
        ('vesel', 'tisti, ki izraža veselje'),
        ('žaga', 'orodje za žaganje'), ...,
        ('razsvetljenstvo', 'zgodovinsko obdobje, znano po žarnicah')]
```

Postopek za iskanje je podoben prejšnjemu, le da se tokrat vozimo čez pare in ključe primerjamo z iskanim. Če najdemo ujemajoč ključ, vrnemo pripadajočo vrednost, sicer pa vrnemo `None`.

```
def poisci_vrednost_v_neurejenem(seznam, iskani_kljuc):

:   """Vrne pripadajočo vrednost ključa v seznamu. Ce je ni, vrne
    None.""" for kljuc, vrednost in seznam: if kljuc ==
    iskani_kljuc: return vrednost return None
```

```
```
```{code-cell}
poisci_vrednost_v_neurejenem([(7, 'a'), (4, 'r'), (8,
't')], 7) 'a'
```
```{code-cell}
poisci_vrednost_v_neurejenem([(7, 'a'),
(4, 'r'), (8, 't')], 5)
>>>```
```{code-cell}
poisci_vrednost_v_neurejenem([(7, 'a'), (4, 'r'), (8, 't')],
'r')
```

Tudi v zadnjem klicu smo dobili rezultat `None`, saj se `'r'` v seznamu pojavi le kot vrednost, ne kot ključ.

Če je seznam urejen, lahko iskani element poiščemo bistveno hitreje z bisekcijo. V seznamu si pogledamo element na sredini. Če je slučajno enak iskanemu elementu, smo končali, sicer pa je bodisi večji bodisi manjši. Če je sredinski element večji od iskanega, potem vemo, da se iskani element ne more pojaviti v desni polovici, saj so vsi tamkajšnji elementi zaradi urejenosti večji od sredinskega. Tako lahko iskanje zožimo le na levo polovico seznama. Če je sredinski element manjši od iskanega, pa iskanje zožimo na desno polovico seznama. V obeh primerih iskanje nadaljujemo na polovico manjšem seznamu, kjer uporabimo enak postopek. To nadaljujemo dokler iskanja ne zožimo na seznam dolžine 1\. V tem primeru le pogledamo, če je edini element enak iskanemu. Če je, smo iskani element našli, če ni, pa ga v seznamu ni bilo.

Bisekcijo lahko implementiramo na več načinov. Prvi je, da v spremenljivkah `zacetek` in `konec` hranimo začetni in končni indeks podseznama, v katerem iščemo element. V skladu s Pythonovimi standardi, v spremenljivki `konec` ne bomo hranili zadnjega indeksa v podseznamu, temveč naslednji indeks. Na začetku bomo element iskali v celotnem seznamu, zato bo `zacetek` enak 0, `konec` pa dolžini seznama. Odvisno od tega, kakšen je sredinski element v primerjavi z iskanim, bomo spremenljivki `zacetek` in `konec` ustrezno popravljali. Ko se indeksa izenačita, postopek končamo, saj je tedaj podseznam prazen.

```
def poisci_v_urejenem_z_zanko(seznam, iskani_element):

:   """Vrne True, če se iskani element pojavi v urejenem seznamu, in
    False, če se ne.""" zacetek = 0 konec = len(seznam)

    while zacetek < konec:

    :   sredina = (zacetek + konec) // 2 if seznam[sredina] ==
        iskani_element: return True elif seznam[sredina] <
        iskani_element: zacetek = sredina + 1 elif seznam[sredina] >
        iskani_element: konec = sredina

    return False
```

```
```
```{code-cell}
poisci_v_urejenem_z_zanko([1, 2, 3, 5], 4) False
>>>```
```{code-cell}
poisci_v_urejenem_z_zanko([1, 2, 3, 5], 3) True
```

Seveda funkcija ne bo delala pravilno, če ji ne bomo podali urejenega seznama:

```
```
```{code-cell}
poisci_v_urejenem_z_zanko([3, 3, 3, 1, 5, 5, 5], 3) False
```

Enak postopek zapišemo tudi rekurzivno, vendar moramo biti pri tem malo bolj previdni. Načeloma lahko iskanje v podseznamu naredimo tako, da s pomočjo rezin ustvarili manjši seznam in iščemo v njem:

```
def poisci_v_urejenem_z_rezinami(seznam, iskani_element):

:   """Vrne True, če se iskani element pojavi v urejenem seznamu, in
    False, če se ne.""" if len(seznam) == 0: return False else:
    sredina = len(seznam) // 2 if seznam[sredina] == iskani_element:
    return True elif seznam[sredina] < iskani_element: return
    poisci_v_urejenem_z_rezinami(seznam[sredina + 1:],
    iskani_element) elif seznam[sredina] > iskani_element: return
    poisci_v_urejenem_z_rezinami(seznam[:sredina],
    iskani_element)
```

```
```
```{code-cell}
poisci_v_urejenem_z_rezinami([1, 2, 3, 5], 4) False
>>>```
```{code-cell}
poisci_v_urejenem_z_rezinami([1, 2, 3, 5], 3) True
```

Taka funkcija sicer deluje pravilno, vendar opravlja nepotrebno delo, saj ob vsakem rekurzivnem klicu naredi novo rezino (bodisi `seznam[sredina + 1:]` bodisi `seznam[:sredina]`), kar zahteva, da vse ustrezne elemente presname na novo mesto. Bolje je, da tako kot pri rešitvi z zankami ves čas delamo z istim seznamom, vendar si zapomnimo, med katerima dvema indeksoma iščemo element.

```
def poisci_v_urejenem_med_indeksoma(seznam, iskani_element, zacetek, konec):

:   """Vrne True, če se iskani element pojavi v urejenem seznamu na
    mestu i, kjer je zacetek <= i < konec, in False, če se ne."""
    if zacetek == konec: return False else: sredina = (zacetek + konec)
    // 2 if seznam[sredina] == iskani_element: return True elif
    seznam[sredina] < iskani_element: return
    poisci_v_urejenem_med_indeksoma(seznam, iskani_element,
    sredina + 1, konec) elif seznam[sredina] > iskani_element:
    return poisci_v_urejenem_med_indeksoma(seznam, iskani_element,
    zacetek, sredina)
```

```
```
```{code-cell}
poisci_v_urejenem_med_indeksoma([1, 2, 3, 5], 4, 0, 3)
False
```
```{code-cell}
poisci_v_urejenem_med_indeksoma([1, 2, 3, 5], 3, 0,
3) True
```
```{code-cell}
poisci_v_urejenem_med_indeksoma([1, 2, 3, 5], 3, 0,
2) False
```

Ta rešitev je veliko bolj učinkovita, saj ne ustvarja novih elementov, je pa malo moteče, ker moramo vsakič podajati meje. Če tega ne želimo, lahko uporabimo bodisi pomožno funkcijo:

```
def poisci_v_urejenem(seznam, iskani_element):

:   """Vrne True, če se iskani element pojavi v urejenem seznamu, in
    False, če se ne.""" return
    poisci_v_urejenem_med_indeksoma(seznam, iskani_element, 0,
    len(seznam))
```

bodisi argumentoma `zacetek` in `konec` damo privzeti vrednosti:

```
def poisci_v_urejenem_med_indeksoma(seznam, iskani_element, zacetek=0, konec=None):

:   """Vrne True, če se iskani element pojavi v urejenem seznamu na
    mestu i, kjer je zacetek <= i < konec, in False, če se ne."""
    if konec is None: konec = len(seznam)

    if zacetek == konec:

    :   return False

    else:

    :   sredina = (zacetek + konec) // 2 if seznam[sredina] ==
        iskani_element: return True elif seznam[sredina] <
        iskani_element: return
        poisci_v_urejenem_med_indeksoma(seznam, iskani_element,
        sredina + 1, konec) elif seznam[sredina] > iskani_element:
        return poisci_v_urejenem_med_indeksoma(seznam,
        iskani_element, zacetek, sredina)
```

```
```
```{code-cell}
poisci_v_urejenem_med_indeksoma([1, 2, 3, 5], 3, 0, 3) True
```
```{code-cell}
poisci_v_urejenem_med_indeksoma([1, 2, 3, 5], 3) True
```
```{code-cell}
poisci_v_urejenem_med_indeksoma([1, 2, 3, 5], 3, 0, 2)
False
```

Kot vidimo, smo privzeto vrednost argumenta `zacetek` nastavili na 0, privzete vrednosti argumenta `konec` pa nismo nastavili na dolžino seznama. Razlog je v tem, da vrednost privzetega argumenta lahko nastavimo le enkrat: takrat, ko funkcijo definiramo. Ker pa hočemo funkcijo uporabiti na seznamih različnih dolžin, nobena privzeta vrednost ne bo prava. Običajna rešitev je, da argumentom, za katere lahko privzete vrednosti izračunamo šele ob klicu funkcije, nastavimo privzeto vrednost `None`. Nato pa ob klicu funkcije v primerih, ko se je uporabila ta privzeta vrednost, vrednost argumenta ustrezno popravimo. V našem primeru smo takrat, ko je bila vrednost spremenljivke `konec` enaka `None`, njeno vrednost nastavili na dolžino danega seznama. V primeru, ko smo ob klicu funkcije vrednost argumenta `konec` podali (torej ob rekurzivnih klicih), pa bo ta vrednost različna od `None`, zato se ne bo zgodilo nič.
