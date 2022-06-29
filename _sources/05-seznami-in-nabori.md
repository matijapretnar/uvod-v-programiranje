---
jupytext:
  cell_metadata_filter: '-all'
  formats: 'md:myst'
  text_representation:
    extension: .md
    format_name: myst
    format_version: '0.8'
    jupytext_version: 1.5.0
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

(seznami-in-nabori)=

# Seznami & nabori

Če želimo delati z zaporedjem podatkov, uporabimo sezname. Sename pišemo v oglatih oklepajih, med katerimi napišemo vrednosti, ločene z vejicami, na primer `[10, 20, 30]` je seznam, ki vsebuje tri števila, `[]` pa prazen seznam. Če želimo, lahko vejico pišemo tudi za zadnjim elementom. Seznami so lahko tudi gnezdeni. Na primer, matriko bi predstavili s seznamom seznamov `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]`. V sezname lahko spravimo vrednosti različnih tipov, na primer: `[1, True, [2, 5], "Niz", 3.14]` Vendar običajno sezname uporabimo za predstavitev homogene zbirke podatkov, torej da so vse vrednosti istega tipa.

## Osnovne operacije na seznamih

Precej operacij na seznamih je enakih kot na nizih. Sezname lahko stikamo z operacijo `+` in množimo s celimi števili:

```{code-cell}
[True, False] + [True]
```

```{code-cell}
3 * ['x', 'y']
```

Dolžino seznama dobimo s funkcijo `len`:

```{code-cell}
len([100, 200, 300])
```

```{code-cell}
len([])
```

Sezname med seboj primerjamo leksikografsko: najprej prvi par, če sta ta dva enaka, naslednji par in tako naprej.

```{code-cell}
[1, 100, 10000] < [2, 0, 0]
```

Prav tako imamo na voljo predikata `in` in `not in`, s katerima ugotovimo, ali se nek element pojavlja v seznamu:

```{code-cell}
prastevila = [2, 3, 5, 7, 11, 13, 17]
5 in prastevila
```

```{code-cell}
15 not in prastevila
```

Predikat `in` na seznamih se razlikuje od tistega na nizih v tem, da preverja le pojavitev elementov, ne pa podseznamov:

```{code-cell}
[3, 5, 7] in prastevila
```

Na primer:

```{code-cell}
def stevilo_dni(mesec, leto):
    if mesec == 2:
        return 29 if je_prestopno(leto) else 28
    elif mesec in [4, 6, 9, 11]:
        return 30
    else:
        return 31
```

Indeksiranje in rezine na seznamih delujejo tako kot na nizih:

```{code-cell}
prastevila = [2, 3, 5, 7, 11, 13, 17]
```

```{code-cell}
prastevila[2]
```

```{code-cell}
prastevila[-2]
```

```{code-cell}
prastevila[len(prastevila) - 2]
```

```{code-cell}
prastevila[2:-2]
```

```{code-cell}
prastevila[::2]
```

Če imamo gnezdene sezname, do elementov dostopamo z gnezdenimi indeksi:

```{code-cell}
mat = [[1, 0, 0], [0, -1, 2], [3, 1, 5]]
mat[1][-1]
```

Na primer, sled matrike bi lahko izračunali kot:

```{code-cell}
def sled(matrika):
    """Izračuna sled dane matrike."""
    vsota_diagonalnih = 0
    for i in range(len(matrika)):
        vsota_diagonalnih += matrika[i][i]
    return vsota_diagonalnih
```

```{code-cell}
mat = [[5]]
```

```{code-cell}
sled(mat)
```

Sledi pa nikakor ne bomo izračunali na sledeči (pri študentih dostikrat videni) način:

```{code-cell}
def grozna_sled(matrika):
    """Na popolnoma napačen izračuna sled dane matrike."""
    vsota_diagonalnih = 0
    for i in range(len(matrika)):
        for j in range(len(matrika)):
            if i == j:
                vsota_diagonalnih += matrika[i][j]
    return vsota_diagonalnih
```

Funkcija sled matrike sicer izračuna pravilno, vendar na izjemno potraten način, saj se sprehodi čez celotno matriko, ne le čez diagonalne elemente. Na primer, pri matriki velikosti $1000 \times 1000$ bi druga funkcija pregledala tisočkrat več elementov (in posledično porabila tisočkrat več časa).

## Zanke na seznamih

Tako kot se lahko z zanko `for` sprehodimo po vseh znakih v nizu, se lahko z njo sprehodimo tudi po vseh elementih danega seznama:

```{code-cell}
for x in [10, 20, 30]:
    print(x)
```

Na primer, vsoto vseh elementov seznama bi definirali kot:

```{code-cell}
def vsota_elementov(seznam):
    """Vrne vsoto elementov v danem seznamu."""
    vsota = 0
    for element in seznam:
        vsota += element
    return vsota
```

```{code-cell}
vsota_elementov([10, 2, 4000, 300])
```

Največji element v danem seznamu lahko poiščemo tako, da zaporedoma vsak element seznama primerjamo z do sedaj največjim videnim elementom. Če je trenutni element večji, do sedaj največji element popravimo. Ko pregledamo vse elemente v seznamu, je do sedaj največji element tudi na splošno največji element. Edina stvar, na katero moramo še paziti, je ta, da na začetku izberemo ustrezen največji element. Tu imamo dve dobri izbiri. (Slaba izbira bi bila, da bi za največji do zdaj viden element vzeli neko dovolj majhno število, na primer 0 ali -9999999 -- ta izbira je očitno napačna!) Prva dobra izbira je kar prvi element v seznamu, pri čemer moramo potem poprej preveriti še to, da je seznam neprazen:

```{code-cell}
def najvecji_element(seznam):
    """Vrne največji element v danem seznamu. Če ga ni, vrne None"""
    if len(seznam) == 0:
        return
    najvecji_do_zdaj = seznam[0]
    for element in seznam:
        if element > najvecji_do_zdaj:
            najvecji_do_zdaj = element
    return najvecji_do_zdaj
```

```{code-cell}
najvecji_element([10, 2, 4000, 300])
```

Seveda lahko uporabimo tudi vgrajene funkcije:

```{code-cell}
sum([10, 2, 4000, 300])
```

```{code-cell}
min([10, 2, 4000, 300])
```

```{code-cell}
max([10, 2, 4000, 300])
```

## Spreminjanje seznamov

Za razliko od nizov lahko vrednosti v seznamih tudi spreminjamo:

```{code-cell}
sez = [10, 20, 30]
sez[1]
```

```{code-cell}
sez[1] = 40
sez
```

Zamenjamo lahko tudi celotno **rezino**

```{code-cell}
sez = [10, 20, 30, 40]
sez[1:3]
[20, 30]
```

```{code-cell}
sez[1:3] = [0, 0, 0]
sez
```

Če nadomestna rezina ni enake dolžine kot prvotna, se seznam ustrezno skrajša ali podaljša. Nadomestimo tudi prazno rezino, s čimer nove elemente vrinemo v seznam. Nadomeščanje prazne rezine ni isto kot nadomeščanje elementa z istim indeksom kot rezina:

```{code-cell}
sez = [10, 20, 30, 40]
sez[2:2] = [0, 0, 0]
sez
```

```{code-cell}
sez = [10, 20, 30, 40]
sez[2] = [0, 0, 0]
sez
```

Tako elemente kot rezine lahko tudi **brišemo**

```{code-cell}
sez = [10, 20, 30, 40, 50]
del sez[1]
sez
```

```{code-cell}
sez = [10, 20, 30, 40, 50]
del sez[2:4]
```

Pri spreminjanju seznamov je treba biti previden, saj ne deluje tako, kot smo navajeni pri spreminjanju vrednosti spremenljivk. Na primer, če pišemo

```{code-cell}
a = 5
b = a
a = 0
b
```

Vidimo, da se vrednost spremenljivke `b` ni spremenila, ko smo spremenili `a`, saj smo jo v drugi vrstici nastavili na število 5\. Pri seznamih je stvar malo drugačna. Če pišemo

```{code-cell}
a = [1, 1, 1]
b = a
a = [2, 2, 2]
b
```

so stvari še vedno take, kot bi jih pričakovali. Vrednost `b` smo nastavili na isti seznam kot `a`, vendar smo potem rekli, da naj bo v `a` shranjen drugačen seznam, s čimer na vrednost v `b` nismo vplivali. Če pa pišemo

```{code-cell}
a = [1, 1, 1]
b = a
a[1] = 2
b
```

se je s tem, ko smo spremenili `a`, spremenil tudi `b`. Kaj se je zgodilo? Ko smo napisali `b = a`, smo povedali, naj bo v `b` shranjen isti seznam kot `a`. In z `a[1] = 2` smo povedali, naj se na mesto `1` v seznamu, shranjenem v `a`, zapiše 2\. Ker je v `b` shranjen isti (ne le enak) seznam kot v `a`, je s tem tudi seznam v `b` drugačen. Da je zmeda večja, `+=` ni samo okrajšava za `=` in `+`, kot smo navajeni pri številih:

```{code-cell}
a = [1, 1, 1]
b = a
a = a + [2, 2, 2]
b
```

```{code-cell}
a = [1, 1, 1]
b = a
a += [2, 2, 2]
b
```

V prvem primeru izračunamo nov seznam `a + [2, 2, 2]` in ga shranimo pod ime `a`, s čimer se `b` ne spremeni. V drugem primeru pa je `+=` operacija, ki razširi obstoječi seznam. Ker gre pri `a` in `b` za isti seznam, se spremeni tudi seznam v `b`.

Pogosta past, v katero se na začetku ujamemo zaradi spremenljivosti seznamov, je izračun identične matrike. Vemo že, da lahko v Pythonu seznam pomnožimo s številom:

```{code-cell}
3 * [0]
```

To nam da idejo, da bi lahko na isti način izračunali ničelno matriko:

```{code-cell}
3 * [3 * [0]]
```

Izračun je videti pravilen, vendar vse tri vrstice te matrike kažejo na isti seznam. To je tako, kot če bi pisali:

```{code-cell}
vrstica = [0, 0, 0]
```

```{code-cell}
matrika = [vrstica, vrstica, vrstica]
```

Poskusimo iz te matrike dobiti identično matriko tako, da po diagonali nastavimo enice. Najprej nastavimo prvi element v prvi vrstici:

```{code-cell}
matrika[0][0] = 1
matrika
```

Kaj se je zgodilo? Ker druga in tretja vrstica kažeta na isti seznam kot prva, smo tudi v njima prvi element popravili na 1\. Če sedaj nastavimo še drugi element v drugi vrstici in tretjega v tretji vrstici se zgodba ponovi:

```{code-cell}
matrika[1][1] = 1
matrika[2][2] = 1
matrika
```

Če želimo identično matriko izračunati na pravilen način, moramo za predstavitev vsake vrstice podati svoj seznam, zato ne moremo uporabiti le pomnoževanja seznamov.

## Vgrajene metode na seznamih

Kot pri nizih za večino pogosto uporabljanih stvari na seznamih obstajajo že vgrajene metode. Te povečini ne vračajo ničesar, temveč le spremenijo dani seznam. Izjemi sta metodi `index` in `count`, ki vrneta vrednost in seznam pustita pri miru, ter metoda `pop` ki tako spremeni seznam kot vrne vrednost. Vse metode so naštete v [uradni dokumentaciji](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists), najbolj osnovne izmed njih pa so:

- `sez.append(x)` na konec seznama `sez` doda element `x`.

```{code-cell}
sez = [10, 20, 30]
sez.append(40)
sez
```

Metodo `append` pogosto uporabljamo za izračun seznama ustreznih elementov. To storimo tako, da ustvarimo prazen seznam, nato pa vanj z metodo `append` dodamo vsak ustrezen element. To je podoben postopek kot pri izračunu vsote ustreznih elementov, kjer smo ustvarili spremenljivko z začetno vrednostjo 0, nato pa ji prištevali ustrezne elemente.

- `sez.extend(sez2)` na konec seznama `sez` doda vse elemente iz seznama `sez2`.

```{code-cell}
sez = [10, 20, 30]
sez.extend([40, 50])
sez
```

Okrajšava `+=`, ki smo jo videli prej, pokliče natanko metodo `extend`.

```{code-cell}
sez = [10, 20, 30]
sez += [40, 50]
sez
```

- `sez.insert(i, x)` pred element na mestu `i` v seznamu `sez` vstavi element `x`.

```{code-cell}
sez = [10, 20, 30]
sez.insert(1, 0)
sez
[10, 0, 20, 30]
```

- `sez.remove(x)` iz seznama `sez` odstrani prvo pojavitev vrednosti `x`.

```{code-cell}
sez = [1, 2, 1, 2, 3]
sez.remove(2)
sez
```

- `sez.pop(i=-1)` vrne element na mestu `i` v seznamu `sez` in odstrani ta element iz seznama. Če indeksa `i` ne podamo, metoda odstrani zadnji element.

```{code-cell}
sez = [10, 20, 30]
sez.pop()
```

```{code-cell}
sez
```

- `sez.clear()` iz seznama `sez` pobriše vse elemente.

```{code-cell}
sez = [1, 2, 1, 2, 3]
sez.clear()
sez
```

- `sez.index(x)` vrne prvo mesto, na katerem se v seznamu `sez` nahaja vrednost `x`.

- `sez.count(x)` vrne število pojavitev vrednosti `x` v seznamu `sez`.

- `sez.sort(key=None, reverse=False)` na mestu uredi seznam glede na vrednosti funkcije `key`. Če parameter `reverse` nastavimo na `True`, bo seznam urejen padajoče.

```{code-cell}
sez = [4, 1, 8, 2, 16]
sez.sort()
sez
```

```{code-cell}
sez = [4, 1, 8, 2, 16]
sorted(sez)
[1, 2, 4, 8, 16]
```

- `sez.reverse()` obrne seznam `sez` na glavo.

```{code-cell}
sez = [1, 2, 4, 8, 16]
sez.reverse()
sez
```

TODO: primerjava z rezinami

```{code-cell}
sez = [1, 2, 4, 8, 16]
sez[::-1]
sez
```

## Izpeljani seznami

Sezname dostikrat lepše zgradimo z _izpeljanimi seznami_, ki so oblike `[izraz for spremenljivka in mozne_vrednosti]`. Podobno kot v matematiki množice pišemo kot ${ 2 \cdot n \mid n \in {1, \dots, 9}}$, lahko v Pythonu napišemo seznam:

```{code-cell}
[2 * n for n in range(1, 10)]
```

ali pa na primer:

```{code-cell}
potence = [2 ** n for n in range(10)]
potence
```

```{code-cell}
[n - 1 for n in potence]
```

```{code-cell}
[int(stevka) for stevka in str(3141592)]
```

Če želimo, lahko v izpeljani seznamih oblike `[izraz for spremenljivka in mozne_vrednosti if pogoj]` s pogojem določimo, katere elemente želimo:

```{code-cell}
[2 * n for n in range(1, 10) if n % 3 == 1]
```

```{code-cell}
def vsota_pozitivnih_elementov(seznam):
    """Vrne seznam vseh pozitivnih elementov danega seznama."""
    return sum([element for element in seznam if element > 0])
vsota_pozitivnih_elementov([10, -20, 50])
```

Zanke v izpeljanih seznamih so lahko gnezdene na dva načina. Prvi je, da kot elemente izpeljanega seznama spet podamo izpeljane sezname. Na primer, identično matriko lahko naredimo kot:

```{code-cell}
def identicna_matrika(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]
```

Lahko pa v izpeljanem seznamu naštejemo več zank, pri čemer ob vsakem koraku v obhodu prve spremenljivke naredimo obhod vseh preostalih:

```{code-cell}
def razlicni_pari(n):
    return [(i, j) for i in range(n) for j in range(i, n)]
razlicni_pari(5)
```

Izpeljani seznami pa niso vedno rešitev, tudi če so krajši. Na primer, če je vsaka vrednost v seznamu odvisna od prejšnjih, jih ne moremo uporabiti.

## Nabori

Nabori so prav tako kot seznami sestavljeni iz več elementov, pišemo pa jih med običajne oklepaje: `(1, 2, 3)`. Nabor z enim elementom pišemo kot `(1, )` (razmislite, zakaj ga ne pišemo kot `(1)`). Namen naborov je hranjenje heterogenih podatkov. To pomeni, da imajo elementi na različnih mestih različne pomene. Na primer, če vemo da vsako število v seznamu `[103, 111, 98, 106]` predstavlja rezultat neke meritve, bi podobno sklepali tudi, če bi v seznam dodali še kakšno drugo številko. Pri datumu `(25, 6, 1991)` pa imajo različne komponente različne pomene: prva predstavlja dan, druga mesec in tretje leto. Če bi dodali še četrto številko, bi morali povedati, kaj pomeni. Python nam seveda omogoča, da bi meritve zapisali kot `(103, 111, 98, 106)`, datum pa kot `[25, 6, 1991]`, vendar bomo sezname uporabljali za **poljubno število podatkov z enakim pomenom**, nabore pa za **fiksno število podatkov z različnimi pomeni**.

S tem namenom so nabori v Pythonu nespremenljivi:

```{code-cell}
:tags: ["raises-exception"]
x = (1, 1, 1)
x[2] = 2
```

Sicer pa za nabore veljajo podobne lastnosti kot za sezname: lahko jih stikamo in množimo; lahko izračunamo njihovo vsoto, minimum, maksimum in dolžino; s predikatom `in` lahko pogledamo, ali vsebujejo dani element; lahko jih indeksiramo in delamo rezine; po njih se lahko sprehodimo z zanko `for`; od metod pa sta na voljo le `count` in `index`, saj ti dve edini ne spreminjata ničesar.

```{code-cell}
(True, False) + (True,)
```

```{code-cell}
3 * ('x', 'y')
```

```{code-cell}
5 in (1, 2, 3)
```

```{code-cell}
(1, 2, 5, 10, 20, 50)[3]
```

```{code-cell}
(1, 2, 5, 10, 20, 50)[3:]
```

Če imamo nabor, ga lahko razstavimo na posamezne spremenljivke, na primer

```{code-cell}
datum = (25, 6, 1991)
dan, mesec, leto = datum
f'{dan}. {mesec}. {leto}'
```

V resnici gre pri hkratnem prireditvenem stavku kot je

```{code-block}
x, y = 10, 20
```

za to, da najprej naredimo torej nabor z dvema komponentama oziroma par `(10, 20)`, nato pa ga razstavimo na dve spremenljivki.

## Funkciji `enumerate` in `zip`

Dostikrat želimo hkrati dostopati do elementov seznama in njihovih indeksov.

Predstavimo polinome s seznamom koeficientov, urejenim od prostega proti vodilnemu členu. Polinom $3 - x^2$ bi tako predstavili s seznamom `[3, 0, -1]`. Pri izračunu vrednosti polinoma želimo hkrati dostopati tako do koeficientov kot do njihovih indeksov, ki ustrezajo potenci. To lahko storimo na več načinov. Lahko se vozimo po indeksih in prek njih dostopamo do koeficientov:

```{code-cell}
def vrednost_polinoma(polinom, x):
    vsota = 0
    for i in range(len(polinom)):
        koef = polinom[i]
        vsota += koef * x ** i
    return vsota
```

```{code-cell}
vrednost_polinoma([3, 0, 1], 1)
```

```{code-cell}
vrednost_polinoma([3, 0, 1], 2)
```

Lahko se vozimo po koeficientih in hkrati povečujemo števec indeksa:

```{code-cell}
def vrednost_polinoma(polinom, x):
    vsota = 0
    i = 0
    for koef in polinom:
        vsota += koef * x ** i
        i += 1
    return vsota
```

````{warning}
Paziti moramo, da indeksa ne računamo s pomočjo metode `index`, saj ta vrne indeks prve pojavitve iskane vrednosti, kar je narobe (pa še počasno):

    ```{code-cell}
    def napacna_vrednost_polinoma(polinom, x):
        vsota = 0
        for koef in polinom:
            i = polinom.index(koef)
            vsota += koef * x ** i
        return vsota
````

````
```{code-cell}
vrednost_polinoma([0, 2, 0, 2], 3)
```

```{code-cell}
napacna_vrednost_polinoma([0, 2, 0, 2], 3)
```
````

````
Ker je v spodnjem klicu funkcije metoda `index` za indeks prve pojavitve vrednosti 2 obakrat vrnila 1, je funkcija vrnila $2 \cdot 3^1 + 2 \cdot 3^1 = 6$ namesto $2 \cdot 3^1 + 2 \cdot 3^3 = 60$.

Najbolj enostavno pa je, da uporabimo funkcijo `enumerate`, ki zaporedoma vrača pare, v katerih so druge komponente vrednosti danega seznama, prve komponente pa njihovi indeksi:

```{code-cell}
for x in enumerate('abc'):
    print(x)
````

Pare, ki nam jih podaja `enumerate` lahko v dve spremenljivki razstavimo tudi v zanki `for`:

```{code-cell}
for i, x in enumerate('abc'):
    print(i, x)
```

S pomočjo funkcije `enumerate` lahko vrednost polinoma izračunamo kot:

```{code-cell}
def vrednost_polinoma(polinom, x):
    vsota = 0
    for i, koef in enumerate(polinom):
        vsota += koef * x ** i
    return vsota
```

ali še krajše z izpeljanim seznamom:

```{code-cell}
def vrednost_polinoma(polinom, x):
    return sum([koef * x ** i for i, koef in enumerate(polinom)])
```

Podobno kot `enumerate` deluje funkcija `zip`, ki sprejme več seznamov, vrne pa zaporedje naborov istoležnih elementov:

```{code-cell}
for x in zip('xyz', [10, 20, 30], [4, 5, 6]):
    print(x)
```

Funkciji se reče `zip`, ker združuje elemente različnih seznamov tako kot zadrga. Vrnjeno zaporedje ima toliko elementov, kot najkrajši argument funkcije:

```{code-cell}
for x in zip('xyz', [10, 20, 30, 40]):
    print(x)
```

S pomočjo funkcije `zip` lahko enostavno izračunamo skalarni produkt:

```{code-cell}
def skalarni_produkt(vektor1, vektor2):
    """Vrne skalarni produkt dveh vektorjev iste dimenzije."""
    assert len(vektor1) == len(vektor2)
    vsota = 0
    for x1, x2 in zip(vektor1, vektor2):
        vsota += x1 * x2
    return vsota
```

ali kot:

```{code-cell}
def skalarni_produkt(vektor1, vektor2):
    """Vrne skalarni produkt dveh vektorjev iste dimenzije."""
    assert len(vektor1) == len(vektor2)
    return sum([x1 * x2 for x1, x2 in zip(vektor1, vektor2)])
```

```{code-cell}
skalarni_produkt([1, -2, 5], [-2, 5, 2])
```
