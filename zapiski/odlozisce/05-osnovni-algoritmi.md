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

## Evklidov algoritem

Algoritem je zaporedje korakov, s katerimi dobimo iskani rezultat. Načeloma lahko pod besedo algoritem razumemo tudi zaporedje korakov, s katerimi si skuhamo jajca (vzemi posodo; odpri pipo; postavi posodo pod pipo; ko je posoda dovolj polna, zapri pipo; ...), ampak mi si jo bomo prihranili za postopke, s katerimi izračunamo želene vrednosti.

Za prvi algoritem se spodobi, da si pogledamo najstarejši znani algoritem in sicer Evklidov algoritem za iskanje navečjega skupnega delitelja dveh števil. Naj bo $d$ največji skupni delitelj števil $m$ in $n$. Pišimo $m = k \cdot n + o$, kjer je $0 \le o < n$. Torej: $o$ je ostanek pri deljenju števila $m$ z $n$. Ker e $d$ deli $n$, deli tudi $k \cdot n$. Poleg tega $d$ deli tudi $m$, zato deli tudi $o = m - k \cdot n$. Velja tudi obratno, če $d$ deli $n$ in $o$, potem deli tudi $m = k \cdot n + o$.

Zato lahko iskanje največjega skupnega delitelja števil $m$ in $n$ prevedemo na iskanje največjega skupnega delitelja števil $n$ in $o$. Videti je, kot da se vrtimo v krogu, vendar se ne. Poglejmo, kaj se zgodi:

1. Največji skupni delitelj števil $456$ in $123$ je enak največjemu skupnemu delitelju števil $123$ in $456 - 3 \cdot 123 = 87$.
2. Največji skupni delitelj števil $123$ in $87$ je enak največjemu skupnemu delitelju števil $87$ in $123 - 1 \cdot 87 = 36$.
3. Največji skupni delitelj števil $87$ in $36$ je enak največjemu skupnemu delitelju števil $36$ in $123 - 2 \cdot 36 = 15$.
4. Največji skupni delitelj števil $36$ in $15$ je enak največjemu skupnemu delitelju števil $15$ in $36 - 2 \cdot 15 = 6$.
5. Največji skupni delitelj števil $15$ in $6$ je enak največjemu skupnemu delitelju števil $6$ in $15 - 2 \cdot 6 = 3$.
6. Največji skupni delitelj števil $6$ in $3$ je enak največjemu skupnemu delitelju števil $3$ in $6 - 2 \cdot 3 = 0$.

Postopka ne moremo več nadaljevati, ker ne moremo deliti z nič. Kaj pa je največji skupni delitelj števil 3 in 0? Ja, 3 vendar. Torej, ko je drugo število enako 0, je prvo število ravno njun največji skupni delitelj, po vseh prejšnjih sklepih pa tudi največji skupni delitelj vseh prejšnjih parov vključno s prvim.

Evklidov algoritem je torej sledeč: če je $n = 0$, potem je največji skupni delitelj števil $m$ in $n$ enak kar $m$, sicer pa je enak največjemu skupnemu delitelju števil $n$ in $o$, kjer je $o$ ostanek pri deljenju $m$ z $n$. Ta postopek enostavno prevedemo v Python:

```
def gcd(m, n):

:   

    if n == 0:

    :   return m

    else:

    :   return gcd(n, m % n)
```

ali s pogojnim izrazom kot

```
def gcd(m, n):

:   '''Vrne največji skupni delitelj števil m in n.''' return m if
    n == 0 else gcd(n, m % n)
```

Pri tem je `gcd` (_greatest common divisor_) običajna oznaka za največjega skupnega delitelja.

`{code-cell}

> > > gcd(456, 123) 3`

Algoritem deluje tudi, kadar je $n < m$, saj je v tem primeru $n = 0 \cdot m + n$, zato v naslednjem koraku njuni mesti zamenjamo in nadaljujemo kot prej.
